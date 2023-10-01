# !/bin/python3

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route("/")
def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit


@app.route("/")

def index():
    meme_pic,subreddit = get_meme()
    return render_template("template/index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
