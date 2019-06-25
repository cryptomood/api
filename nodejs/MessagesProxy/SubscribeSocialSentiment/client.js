const fs = require("fs");
const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader");

const SERVER = "api.awesome.cryptomood.com:30001";
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

let channel = client.SubscribeSocialSentiment();
channel.on("data", function(message) {
  console.log(message);
});