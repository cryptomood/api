import sys; sys.path.append('../../') # for correct types inclusion,

import grpc

import types_pb2_grpc
from google.protobuf import empty_pb2

SERVER_ADDRESS = 'SERVER'
PATH_TO_CERT_FILE = './cert.pem'


def main():
    # Create credentials for use with an secured channel
    creds = grpc.ssl_channel_credentials(open(PATH_TO_CERT_FILE, 'rb').read())

    # Initialize GRPC channel
    channel = grpc.secure_channel(SERVER_ADDRESS, creds)

    # create stub
    stub = types_pb2_grpc.MessagesProxyStub(channel)

    # Response-streaming RPC
    telegram_stream = stub.SubscribeTelegram(empty_pb2.Empty())
    for telegram in telegram_stream:
        # attributes are same as defined in proto messages
        print(telegram.user_message.base.id, telegram.user_message.message)


if __name__ == '__main__':
    main()
