from flask import Flask, request, json, Response

from services.sentiment_service import get_sentiment
from services.twitter_service import TwitterClient

app = Flask(__name__)
app.config.from_object('config.BaseConfig')
twitter_client = TwitterClient()

@app.route('/')
def hello_world():
    return 'My life for Aiur!'

@app.route('/sentiments/text')
def get_text_sentiment():
    return Response(get_sentiment(request.args.get("value")), content_type="json/application")

@app.route('/sentiments/tweet')
def get_tweet_sentiment():
    parsed_tweets =  twitter_client.get_tweet_sentiment(query=request.args.get("value"))
    return Response(json.dumps(parsed_tweets), content_type="json/application")


if __name__ == '__main__':
    app.run()
