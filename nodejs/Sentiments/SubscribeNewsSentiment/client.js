const fs = require("fs");
const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader");

const SERVER = "SERVER";
const CERT_FILE_PATH = "../../../certs/cert.pem";
const PROTO_FILE_PATH = "../../../types.proto";

const proto = grpc.loadPackageDefinition(
    protoLoader.loadSync(PROTO_FILE_PATH, {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
    })
);

const client = new proto.Sentiments(
    SERVER,
    grpc.credentials.createSsl(fs.readFileSync(CERT_FILE_PATH))
);

var metadata = new grpc.Metadata();

const TOKEN = 'YOUR_TOKEN';
metadata.add('authorization', `Bearer ${TOKEN}`);

let channel = client.SubscribeNewsSentiment({
    resolution: "M1",
    assets_filter: {
        assets: ["BTC", "ETH"],
        all_assets: false
    }
}, metadata);
channel.on("data", function (message) {
    console.log(message);
});