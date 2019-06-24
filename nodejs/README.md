# Cryptomood b2b client - nodejs

# Client example

1.  ensure that you have x509 .pem file (cert.pem). You won't be able to access the server without it
2.  make sure you have at least the latest stable version of Node.js
3.  `npm install`
4.  Load the protobuffer definitions
    
    ```
    const proto = grpc.loadPackageDefinition(
      protoLoader.loadSync("types.proto", {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
      })
    );
    ``` 
    
5.  Initialize the MessagesProxy service. You have to provide valid host address and valid path to .pem file(from 1. step).
    ```
    const client = new proto.MessagesProxy(
      SERVER,
      grpc.credentials.createSsl(fs.readFileSync('./cert.pem'))
    );
    ```
6.  Subscribe to required stream and listen to incoming data
    ```
    let channel = client.SubscribeTweet();
    channel.on("data", function(message) {
      console.log(message);
    });
    ```
    
For full example, see [client.js](./client.js) file in this directory.
For additional resources, see the [grpc library](https://github.com/grpc/grpc-node)
