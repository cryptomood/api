# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import types_pb2 as types__pb2


class MessagesProxyStub(object):
  """*
  Service for pub-sub message model
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SubscribeArticle = channel.unary_stream(
        '/MessagesProxy/SubscribeArticle',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=types__pb2.Article.FromString,
        )
    self.SubscribeTweet = channel.unary_stream(
        '/MessagesProxy/SubscribeTweet',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=types__pb2.Tweet.FromString,
        )
    self.SubscribeReddit = channel.unary_stream(
        '/MessagesProxy/SubscribeReddit',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=types__pb2.RedditPost.FromString,
        )
    self.SubscribeDiscord = channel.unary_stream(
        '/MessagesProxy/SubscribeDiscord',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=types__pb2.DiscordUserMessage.FromString,
        )
    self.SubscribeTelegram = channel.unary_stream(
        '/MessagesProxy/SubscribeTelegram',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=types__pb2.TelegramUserMessage.FromString,
        )
    self.SubscribeBitmex = channel.unary_stream(
        '/MessagesProxy/SubscribeBitmex',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=types__pb2.BitmexUserMessage.FromString,
        )
    self.SubscribeNewsSentiment = channel.unary_stream(
        '/MessagesProxy/SubscribeNewsSentiment',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=types__pb2.SentimentCandle.FromString,
        )
    self.SubscribeSocialSentiment = channel.unary_stream(
        '/MessagesProxy/SubscribeSocialSentiment',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=types__pb2.SentimentCandle.FromString,
        )


class MessagesProxyServicer(object):
  """*
  Service for pub-sub message model
  """

  def SubscribeArticle(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeTweet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeReddit(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeDiscord(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeTelegram(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeBitmex(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeNewsSentiment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeSocialSentiment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MessagesProxyServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SubscribeArticle': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeArticle,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=types__pb2.Article.SerializeToString,
      ),
      'SubscribeTweet': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeTweet,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=types__pb2.Tweet.SerializeToString,
      ),
      'SubscribeReddit': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeReddit,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=types__pb2.RedditPost.SerializeToString,
      ),
      'SubscribeDiscord': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeDiscord,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=types__pb2.DiscordUserMessage.SerializeToString,
      ),
      'SubscribeTelegram': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeTelegram,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=types__pb2.TelegramUserMessage.SerializeToString,
      ),
      'SubscribeBitmex': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeBitmex,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=types__pb2.BitmexUserMessage.SerializeToString,
      ),
      'SubscribeNewsSentiment': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeNewsSentiment,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=types__pb2.SentimentCandle.SerializeToString,
      ),
      'SubscribeSocialSentiment': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeSocialSentiment,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=types__pb2.SentimentCandle.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'MessagesProxy', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class HistoricDataStub(object):
  """*
  Service for requesting historic data
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.HistoricSocialSentiment = channel.unary_unary(
        '/HistoricData/HistoricSocialSentiment',
        request_serializer=types__pb2.SentimentHistoricRequest.SerializeToString,
        response_deserializer=types__pb2.SentimentCandleItems.FromString,
        )
    self.HistoricNewsSentiment = channel.unary_unary(
        '/HistoricData/HistoricNewsSentiment',
        request_serializer=types__pb2.SentimentHistoricRequest.SerializeToString,
        response_deserializer=types__pb2.SentimentCandleItems.FromString,
        )
    self.HistoricTweets = channel.unary_unary(
        '/HistoricData/HistoricTweets',
        request_serializer=types__pb2.HistoricRequest.SerializeToString,
        response_deserializer=types__pb2.TweetItems.FromString,
        )
    self.HistoricArticles = channel.unary_unary(
        '/HistoricData/HistoricArticles',
        request_serializer=types__pb2.HistoricRequest.SerializeToString,
        response_deserializer=types__pb2.ArticleItems.FromString,
        )


class HistoricDataServicer(object):
  """*
  Service for requesting historic data
  """

  def HistoricSocialSentiment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HistoricNewsSentiment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HistoricTweets(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HistoricArticles(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HistoricDataServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'HistoricSocialSentiment': grpc.unary_unary_rpc_method_handler(
          servicer.HistoricSocialSentiment,
          request_deserializer=types__pb2.SentimentHistoricRequest.FromString,
          response_serializer=types__pb2.SentimentCandleItems.SerializeToString,
      ),
      'HistoricNewsSentiment': grpc.unary_unary_rpc_method_handler(
          servicer.HistoricNewsSentiment,
          request_deserializer=types__pb2.SentimentHistoricRequest.FromString,
          response_serializer=types__pb2.SentimentCandleItems.SerializeToString,
      ),
      'HistoricTweets': grpc.unary_unary_rpc_method_handler(
          servicer.HistoricTweets,
          request_deserializer=types__pb2.HistoricRequest.FromString,
          response_serializer=types__pb2.TweetItems.SerializeToString,
      ),
      'HistoricArticles': grpc.unary_unary_rpc_method_handler(
          servicer.HistoricArticles,
          request_deserializer=types__pb2.HistoricRequest.FromString,
          response_serializer=types__pb2.ArticleItems.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'HistoricData', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
