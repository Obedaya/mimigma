FROM python:3.6-alpine

RUN apk --no-cache add postgresql-client

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY user_db_connect.py /usr/src/app/user_db_connect.py
COPY user_config.json /usr/src/app/user_config.json


CMD ["python", "user_db_connect.py"]
