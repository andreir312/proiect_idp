FROM python:alpine

ADD . /vote_app

WORKDIR /vote_app

RUN pip install -r requirements.txt

CMD ["python", "vote_app.py"]
