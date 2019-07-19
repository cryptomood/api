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

const client = new proto.Sentiments(
    SERVER,
    grpc.credentials.createSsl(fs.readFileSync(CERT_FILE_PATH))
);

const now = Date.now() / 1000 | 0; // unix timestamp

let channel = client.HistoricSocialSentiment({
    from: {seconds: now - 7200},
    to: {seconds: now},
    resolution: "H1",
    asset: "BTC"
}, function (err, req) {
    console.log(req, err)
});

channel.on("data", function (message) {
    console.log(message);
});


