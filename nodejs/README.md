# Cryptomood b2b client - nodejs

# Client example

1.  When connecting to the server use x509 cert.pem file located in certs directory. You won't be able to access the server without it
2.  Make sure you have at least the latest stable version of Node.js
3.  `npm install`
4.  Load the protobuffer definitions
    
    ```js
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

5.  Initialize the MessagesProxy service. You have to provide valid host address and valid path to .pem file (from 1. step)
    ```js
    const client = new proto.MessagesProxy(
      SERVER,
      grpc.credentials.createSsl(fs.readFileSync(PATH_TO_CERT_FILE))
    );
    ```

6. Create grpc metadata with your api token (to obtain it visit our [website](https://cryptomood.com/business/products/sentiment-analysis-api/))
    ```js
    var metadata = new grpc.Metadata();
    metadata.add('authorization', `Bearer ${TOKEN}`);
    ```

7.  Subscribe to required stream and listen to incoming data
    ```js
    let channel = client.SubscribeArticle({assets: ["BTC", "ETH"], all_assets: false}, metadata);
    channel.on("data", function(message) {
      console.log(message);
    });
    ```
    
For full example, see any example directory.
For additional resources, see the [grpc library](https://github.com/grpc/grpc-node)
