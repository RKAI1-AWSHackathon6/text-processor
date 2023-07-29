FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-2023-04-17
LABEL maintner="vietnv@rikkeisoft.com"

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ENV TZ="Asia/Ho_Chi_Minh"

COPY . /app
