# !/bin/python3

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


def get_meme():
    url = "https://api.waifu.pics/sfw/shinobu"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["url"]
    return meme_large


@app.route("/")
def index():
    meme_pic = get_meme()
    return render_template("index.html", meme_pic=meme_pic)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
