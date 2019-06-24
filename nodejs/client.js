const fs = require("fs");
const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader");

const SERVER = "<SERVER_ADDRESS>";

const proto = grpc.loadPackageDefinition(
  protoLoader.loadSync("../types.proto", {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true
  })
);

const client = new proto.MessagesProxy(
  SERVER,
  grpc.credentials.createSsl(fs.readFileSync('./cert.pem'))
);

let channel = client.SubscribeTweet();
channel.on("data", function(message) {
  console.log(message);
});