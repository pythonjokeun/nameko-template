FROM python:{{ cookiecutter.python_version }}-alpine

COPY ./Pipfile /Pipfile
COPY ./Pipfile.lock /Pipfile.lock

RUN apk add --no-cache --virtual .build-deps \
    build-base && \
    pip install --no-cache-dir pipenv &&\
    pipenv lock -r > requirements.txt &&\
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps &&\
    rm Pipfile Pipfile.lock requirements.txt

COPY . /{{ cookiecutter.service_name }}

WORKDIR /{{ cookiecutter.service_name }}

CMD nameko run src.service --config config/nameko.yaml
