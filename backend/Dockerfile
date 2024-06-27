FROM python:3.9.19-alpine3.20

## Section to remove CVEs ##
RUN pip install --upgrade pip setuptools
#########

WORKDIR /code

# Install build dependencies
RUN apk add --no-cache gcc musl-dev libc-dev

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
COPY ./app /code/app

EXPOSE 9000

ENV DATABASE_URL=postgresql://db_user:db_pass@db/enigma_db

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000"]
