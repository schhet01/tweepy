
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "465652879-ukMp5wSIr7j7d7QdG8wgG6gNo3XLDcB8nZvk35do"
access_token_secret = "ZeZ9tkaw8udVIGPHcBZIig6UHOVMoykAPmcoSeNRhgSKQ"
consumer_key = "Qz1ayN4ba8IlOW6hbmOPErqGN"
consumer_secret = "x2Xiqq2wdxVAbvGDNsO5zz0Vj43SRdpN0drMYf56f8z3hzWX0H"

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['python', 'javascript', 'ruby'])
