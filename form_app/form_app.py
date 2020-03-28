from flask import Flask, request, render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", port=6379)


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
