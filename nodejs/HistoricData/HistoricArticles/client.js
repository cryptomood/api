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

const client = new proto.HistoricData(
    SERVER,
    grpc.credentials.createSsl(fs.readFileSync(CERT_FILE_PATH))
);

const now = Date.now() / 1000 | 0; // unix timestamp

let channel = client.HistoricArticles({
    from: {seconds: now - 7200},
    to: {seconds: now},
    filter: {assets: ["BTC", "ETH"], all_assets: false}
});
channel.on("data", function (message) {
    console.log(message);
});

