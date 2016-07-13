import tweepy
import pprint
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
from nltk.tokenize import word_tokenize
from collections import Counter
 
# Consumer keys and access tokens, used for OAuth
consumer_key = 'YkpKiOJ65vUjgNZq3PJv8lSLB'
consumer_secret = 'k8lJ4aORn0xUpsFxZsL981ildJuZyA3CXkF3py230gRsMVev3T'
access_token = '752824733738078208-So5vysiFsi5uO5PRdWSjFsDENyWcMXy'
access_token_secret = 'EI2wBzthm0PitKbvZInMlssEmXkdlMWtONjowreMno495'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
# Sample method, used to update a status
#api.update_status('Hello Python Central!')

public_tweets = api.home_timeline()

#for tweet in public_tweets:
# 	  print tweet.text

#x = api.search(q="*",count=100, geocode="29.473410205812087,26.832664700000002,1000km")

#for item in x:
#	print item.text

#news = api.user_timeline(screen_name = 'eahram', count = 100)
#print(type(news))

#for new in news:
#	print(json.dumps(new._json))
 
class MyListener(StreamListener):
    
    def on_data(self, data):
        count_all = Counter()
        try:
            with open('tweets.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#egypt'], locations=[28.96,28.88,33.5,31.39],async=True)
