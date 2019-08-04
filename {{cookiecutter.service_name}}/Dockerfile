FROM python:3.7-alpine as base

FROM base as builder

RUN apk add --update --no-cache build-base &&\
  mkdir install

WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base

RUN apk add --update --no-cache supervisor

COPY --from=builder /install /usr/local
COPY . /gateway

WORKDIR /gateway

CMD ["/usr/bin/supervisord", "-c", "supervisor.conf"]
