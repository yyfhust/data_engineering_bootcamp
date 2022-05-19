

FROM python:3.9.1

WORKDIR /app

COPY Pipfile Pipfile.lock /
COPY postgres_client.py  postgres_client.py 

RUN pip install pipenv
RUN pipenv install --system --deploy

ENTRYPOINT [ "python", "postgres_client.py" ]