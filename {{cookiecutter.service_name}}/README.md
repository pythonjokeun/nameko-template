## Overview

{{ cookiecutter.short_description }}.

## Development

**Running test**

- Run `pytest`

**Running service**

- Spin up a `RabbitMQ` instance at port `5672`
- Run `nameko run src.service --config config/nameko.yaml`

## Structure

- `src/` contains the service logic.
- `test/` contains code used for unit testing using `pytest`.
- `config/` contains configuration files used to run the service.
- `.env` contains environment variables during development.
