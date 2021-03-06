const fs = require("fs");
const assert = require('assert');
const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader");

const SERVER = 'apiv1.cryptomood.com:443';
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

const client = new proto.HistoricData(
    SERVER,
    grpc.credentials.createSsl(fs.readFileSync(CERT_FILE_PATH))
);

var metadata = new grpc.Metadata();

const TOKEN = ''; // put your token here (if you don't have token please visit https://cryptomood.com/business/products/sentiment-analysis-api/

assert(TOKEN != '', 'You need to set TOKEN. To obtain your token visit https://cryptomood.com/business/products/sentiment-analysis-api/.')
metadata.add('authorization', `Bearer ${TOKEN}`);

const now = Date.now() / 1000 | 0; // unix timestamp

let channel = client.HistoricBaseArticles({
    from: {seconds: now - 7200},
    to: {seconds: now},
    filter: {assets: ["BTC", "ETH"], all_assets: false}
}, metadata);
channel.on("data", function (message) {
    console.log(message);
});

