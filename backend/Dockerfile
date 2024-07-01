FROM python:3.9.19-alpine3.20

WORKDIR /code

# Install build dependencies
RUN apk add --no-cache gcc musl-dev libc-dev

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
COPY app /code/app
COPY tests /code/tests
COPY .coveragerc /code/.coveragerc

EXPOSE 9000

ENV DATABASE_URL=postgresql://db_user:db_pass@db/enigma_db
ENV PYTHONPATH=/code

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000"]

# Healthcheck

HEALTHCHECK --interval=10s --timeout=5s --retries=3 CMD curl --fail http://localhost:9000/ || exit 1
