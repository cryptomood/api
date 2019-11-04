const fs = require("fs");
const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader");

const SERVER = "SERVER";
const CERT_FILE_PATH = "./cert.pem";
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

const client = new proto.MessagesProxy(
    SERVER,
    grpc.credentials.createSsl(fs.readFileSync(CERT_FILE_PATH))
);

var metadata = new grpc.Metadata();

// uncomment commands below if token auth is required
// const TOKEN = 'YOUR_TOKEN';
// metadata.add('authorization', `Bearer ${TOKEN}`);

let channel = client.SubscribeBaseTelegram({assets: ["BTC", "ETH"], all_assets: false}, metadata);
channel.on("data", function (message) {
    console.log(message);
});