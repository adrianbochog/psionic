from os import environ

import tweepy
from tweepy import OAuthHandler

from services.sentiment_service import get_sentiment

class TwitterClient(object):
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if TwitterClient.__instance == None:
            TwitterClient()
        return TwitterClient.__instance

    def __init__(self):
        if TwitterClient.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            TwitterClient.__instance = self
            consumer_key = environ.get('CONSUMER_KEY')
            consumer_secret = environ.get('CONSUMER_SECRET')
            try:
                self.auth = OAuthHandler(consumer_key, consumer_secret)
                self.api = tweepy.API(self.auth)
                print("Authentication Successful")
            except:
                print("Error: Authentication Failed")

    def get_tweet_sentiment(self, query, count=10):

        tweets = []

        try:
            fetched_tweets = self.api.search(q=query, count=count)

            for tweet in fetched_tweets:

                parsed_tweet = {}
                parsed_tweet['text'] = tweet.text
                parsed_tweet['sentiment'] = get_sentiment(tweet.text)

                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            return tweets

        except tweepy.TweepError as e:
            print("Error : " + str(e))