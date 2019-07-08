import sys; sys.path.append('../../')  # for correct types inclusion,

import grpc

import types_pb2
import types_pb2_grpc
from google.protobuf import empty_pb2, timestamp_pb2

import time

SERVER_ADDRESS = 'SERVER'
PATH_TO_CERT_FILE = './cert.pem'


def main():
    # Create credentials for use with an secured channel
    creds = grpc.ssl_channel_credentials(open(PATH_TO_CERT_FILE, 'rb').read())

    # Initialize GRPC channel
    channel = grpc.secure_channel(SERVER_ADDRESS, creds)

    # create stub
    stub = types_pb2_grpc.HistoricDataStub(channel)

    now = time.time()
    seconds = int(now)
    to_time = timestamp_pb2.Timestamp(seconds=seconds)
    from_time = timestamp_pb2.Timestamp(seconds=to_time.seconds - int(86400 / 24))  # last hour

    # in our case we have to use kwarg because `from` is
    # is recognized as python keyword so there would syntax be error
    # if you want get value you have to use getattr()
    sentiment_historic_request_kwargs = {'from': from_time, 'to': to_time, 'resolution': 'M1', 'asset': 'BTC',
                                         'allAssets': False}
    req = types_pb2.SentimentHistoricRequest(**sentiment_historic_request_kwargs)
    sentiment_candle_items = stub.HistoricNewsSentiment(req)

    for candle in sentiment_candle_items.items:
        print(candle.id, candle.sentiment_avg)


if __name__ == '__main__':
    main()
