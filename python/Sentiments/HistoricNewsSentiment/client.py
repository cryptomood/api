import sys; sys.path.append('../../')  # for correct types inclusion,

import grpc

import types_pb2
import types_pb2_grpc
from google.protobuf import timestamp_pb2

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
    stub = types_pb2_grpc.SentimentsStub(channel)

    # create timeframe 
    now = time.time()
    seconds = int(now)
    to_time = timestamp_pb2.Timestamp(seconds=seconds - int(86400 / 6))
    from_time = timestamp_pb2.Timestamp(seconds=to_time.seconds - int(2 * 86400)) # last two days

    # in our case we have to use kwarg because `from` is
    # is recognized as python keyword so there would syntax be error
    # if you want get value you have to use getattr()
    sentiment_historic_request_kwargs = { 'from': from_time, 'to': to_time, 'resolution': 'D1', 'asset': 'BTC' }
    req = types_pb2.SentimentHistoricRequest(**sentiment_historic_request_kwargs)
    
    candle_stream = stub.HistoricNewsSentiment(req)
    for candle in candle_stream:
        print(candle.id, candle.a)


if __name__ == '__main__':
    main()
