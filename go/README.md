# Cryptomood b2b client - golang

# Client example

1.  ensure that you have x509 .pem file (cert.pem). You won't be able to access the server without it
2.  make sure you have at least the latest stable version of Golang
3.  (optional) install [protoc tool](https://github.com/golang/protobuf) and [protoc-gen-go](https://github.com/golang/protobuf/tree/master/protoc-gen-go)
4.  (optional) transpile proto file to `*.go` file with `protoc -I .. -I $GOPATH/src --go_out=plugins=grpc:./ ../types.proto`
    This will generate transpiled file into current directory. To adhere golang conventions and also to make these examples work,
    compiler should be able to find this file. Otherwise put it into your GOPATH directory (`$GOPATH/src/types`) and then just import it like
    `import types`.
    
    Steps 3-4 are optional, because this directory already contains prepared `types.pb.go` file
    
5.  Load credentials
    
    ```
    creds, err := credentials.NewClientTLSFromFile(CertFile, "")
    ``` 
    
6.  Dial the server
    ```
	conn, err := grpc.Dial(Server, grpc.WithTransportCredentials(creds), grpc.WithTimeout(5 * time.Second), grpc.WithBlock())
    ```
    
7.  Initialize required service and call required method (in this case subscription)
    ```
	proxyClient := types.NewMessagesProxyClient(conn)
	sub, err := proxyClient.SubscribeTweet(context.Background(), &empty.Empty{})
    ```
    
8.  Read data indefinitely
    ```
    for {
    		msg, err := sub.Recv()
    		if err == io.EOF {
    			continue
    		}
    		if sub.Context().Err() != nil {
    			_ = sub.CloseSend()
    			fmt.Println("Closing connection to server")
    			break
    		}
    		fmt.Println(msg.Base.Content, err)
    	}
    ```
    
For full example, see any example directory.
