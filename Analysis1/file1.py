from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json,time
import twitter_credentials

class StdOutListener(StreamListener):

	def on_data(self,data):
		print(data)

	def on_error(self,status):
		print(status)



if __name__=="__main__":
	listener = StdOutListener()
	auth = OAuthHandler(twitter_credentials.Credentials[0]["API_KEY"], twitter_credentials.Credentials[0]["API_SECRET"])
	auth.set_access_token(twitter_credentials.Credentials[0]["ACCESS_TOKEN"],twitter_credentials.Credentials[0]["ACCESS_TOKEN_SECRET"])
	stream = Stream(auth,listener)
	stream.filter(track=["Narendra Modi"])