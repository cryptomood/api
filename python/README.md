# Cryptomood b2b client - python

# Client example

1.  Ensure that you have x509 .pem file (cert.pem). You won't be able to access the server without it
2.  Make sure you have Python 2.7 or Python 3.4 or higher
3.  Ensure you have `pip` version 9.0.1 or higher 
	`python -m pip install --upgrade pip`
4.  Install gRPC and gRPC tools: 
	```
    python -m pip install grpcio
    python -m pip install grpcio-tools
	```
3.  Generate types `python -m grpc_tools.protoc -I../ --python_out=. --grpc_python_out=. ../types.proto`  
	
	Steps 3 is optional, because this directory already contains prepared `types_pb2.py` and `types_pb2_grpc.py` files 

4.  Create credentials and join channel. You have to provide valid path to .pem file(from 1. step). and  valid host address.  
	```python
    creds = grpc.ssl_channel_credentials(open(PATH_TO_CERT_FILE, 'rb').read())
    channel = grpc.secure_channel(SERVER_ADDRESS, creds)
	``` 
5.  Initialize the MessagesProxy service.  
	```python
    stub = types_pb2_grpc.MessagesProxyStub(channel)
	```
6.  Subscribe to required stream and listen to incoming data  
	```python
    tweet_stream = stub.SubscribeTweet(empty_pb2.Empty())
    for tweet in tweet_stream:
        print(tweet)
	```
    
For full example, see [client.py](./client.py) file in this directory.
For additional resources, see the [grpc library](https://grpc.io/docs/tutorials/basic/python/)
