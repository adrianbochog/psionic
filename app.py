from flask import Flask, request

from services.sentiment_service import get_sentiment

app = Flask(__name__)
app.config.from_object('config.BaseConfig')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/sentiment')
def get_text_sentiment():
    return get_sentiment(request.args.get("text"));


if __name__ == '__main__':
    app.run()
