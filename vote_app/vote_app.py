from flask import Flask, request, render_template
from redis import Redis
from time import sleep

while True:
    try:
        redis = Redis(host="redis", port=6379)
        redis.ping()
    except:
        sleep(1.0)
        continue
    else:
        break

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def vote():
    text = request.form["singles"]
    redis.lpush("singles", text)
    return "<p>Thank you for voting " + text + "!</p>"

app.run(host="0.0.0.0", port=8000)
