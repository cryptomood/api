import sys; sys.path.append('../../') # for correct types inclusion,

import grpc

import types_pb2
import types_pb2_grpc
from google.protobuf import empty_pb2

import time

SERVER_ADDRESS = 'apiv1.cryptomood.com:443'
PATH_TO_CERT_FILE = '../../../certs/cert.pem'
TOKEN = '' # put your token here (if you don't have token please visit https://cryptomood.com/business/products/sentiment-analysis-api/


def main():
    assert TOKEN != '', 'You need to set TOKEN. To obtain your token visit https://cryptomood.com/business/products/sentiment-analysis-api/.'
    # Create credentials for use with an secured channel
    credentials = grpc.ssl_channel_credentials(open(PATH_TO_CERT_FILE, 'rb').read())

    call_credentials = grpc.access_token_call_credentials(TOKEN)
    credentials = grpc.composite_channel_credentials(credentials, call_credentials)

    channel = grpc.secure_channel(SERVER_ADDRESS, credentials)

    # create stub
    stub = types_pb2_grpc.DatasetStub(channel)
    
    asset_items = stub.Assets(empty_pb2.Empty())
    for asset in asset_items.assets:
        print(asset.symbol)



if __name__ == '__main__':
    main()
