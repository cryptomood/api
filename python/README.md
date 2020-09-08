# Cryptomood b2b client - python

# Client example

1.  When connecting to the server use x509 cert.pem file located in certs directory. You won't be able to access the server without it
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

4.  Create credentials and join channel. You have to provide valid path to .pem file (from 1. step), your api token (to obtain it visit our [website](https://cryptomood.com/business/products/sentiment-analysis-api/)) and valid host address.  
	```python
    creds = grpc.ssl_channel_credentials(open(PATH_TO_CERT_FILE, 'rb').read())
	call_creds = grpc.access_token_call_credentials(TOKEN)
    creds = grpc.composite_channel_credentials(creds, call_creds)
    channel = grpc.secure_channel(SERVER_ADDRESS, creds)
	``` 
5.  Initialize the MessagesProxy service.  
	```python
    stub = types_pb2_grpc.MessagesProxyStub(channel)
	```
6.  Subscribe to required stream and listen to incoming data  
	```python
    article_stream = stub.SubscribeArticle(assets_filter)
    for article in article_stream:
        print(article)
	```
    
For full example, see any example directory.
For additional resources, see the [grpc library](https://grpc.io/docs/tutorials/basic/python/)
