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
client.HistoricTweets({ from: { seconds: 1561400800}, to: { seconds: 1561428800}}, function(err, req) {
  console.log(req)
});

