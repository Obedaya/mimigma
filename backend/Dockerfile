FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
COPY ./app /code/app
 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000"]

COPY user_db_connect.py /code/user_db_connect.py

COPY user_config.json /code/user_config.json

RUN pip install psycopg2

CMD ["python3", "user_db_connect.py"]