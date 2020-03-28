from flask import Flask, request, render_template
from redis import Redis
import time

app = Flask(__name__)
while True:
    try:
        redis = Redis(host="redis", port=6379)
    except:
        time.sleep(2)
        continue
    else:
        break


@app.route("/")
def my_form():
    return render_template("my_form.html")


@app.route("/", methods=["POST"])
def my_form_post():
    text = request.form["text"]
    count = redis.incr(text)
    return str(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
