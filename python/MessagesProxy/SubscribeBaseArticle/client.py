import sys; sys.path.append('../../') # for correct types inclusion,

import grpc

import types_pb2
import types_pb2_grpc

SERVER_ADDRESS = 'apiv1.cryptomood.com'
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
    stub = types_pb2_grpc.MessagesProxyStub(channel)

    # create request
    assets_filter = types_pb2.AssetsFilter(assets = ['BTC'], all_assets = False)
    
    # Response-streaming RPC
    article_stream = stub.SubscribeBaseArticle(assets_filter)
    for article in article_stream:
        # attributes are same as defined in proto messages
        print(article.id, article.content)


if __name__ == '__main__':
    main()
