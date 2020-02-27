FROM python:3.8.2-alpine3.11

ADD . /form_app

WORKDIR /form_app

RUN pip install -r requirements.txt

CMD ["python", "form_app.py"]
