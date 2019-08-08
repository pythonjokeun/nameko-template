FROM python:3.7-alpine as base

FROM base as builder

RUN apk add --update --no-cache build-base &&\
  pip install pipenv &&\
  mkdir install

COPY Pipfile /Pipfile
COPY Pipfile.lock /Pipfile.lock

RUN pipenv install &&\
  pipenv lock -r > requirements.txt

WORKDIR /install

RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base

RUN apk add --update --no-cache supervisor

COPY --from=builder /install /usr/local
COPY . /{{ cookiecutter.service_name }}

WORKDIR /{{ cookiecutter.service_name }}

CMD ["/usr/bin/supervisord", "-c", "config/supervisor.conf"]
