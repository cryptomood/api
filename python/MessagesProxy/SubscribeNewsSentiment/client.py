import sys; sys.path.append('../../') # for correct types inclusion,

import grpc

import types_pb2
import types_pb2_grpc


SERVER_ADDRESS = 'SERVER'
PATH_TO_CERT_FILE = './cert.pem'


def main():
    # Create credentials for use with an secured channel
    creds = grpc.ssl_channel_credentials(open(PATH_TO_CERT_FILE, 'rb').read())

    # Initialize GRPC channel
    channel = grpc.secure_channel(SERVER_ADDRESS, creds)
    
    # create stub
    stub = types_pb2_grpc.MessagesProxyStub(channel)

    # create request
    req = types_pb2.CandlesFilter(resolution='M1', asset_filter=types_pb2.AssetsFilter(assets = ['BTC'], all_assets = False))
   
    # Response-streaming RPC
    candle_stream = stub.SubscribeNewsSentiment(empty_pb2.Empty())
    for candle in candle_stream:
        # attributes are same as defined in proto messages
        print(candle.id, candle.sentiment_avg)


if __name__ == '__main__':
    main()
