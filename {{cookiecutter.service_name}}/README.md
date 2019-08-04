## Overview

Describe your service functionality here.

## Development

**Pre-requisite:**

- [pipenv](https://docs.pipenv.org/en/latest/#install-pipenv-today)
- [docker](https://docs.docker.com/install/)

**Setup:**

- Run `cd {{ cookiecutter.service_name }}`
- Run `pipenv install`
- Run `pipenv shell`

**Testing:**

- Run `pytest`

**Running:**

- Make sure you have `RabbitMQ` instance running using port `5672`.
- Run `nameko run src.service --config config/nameko.yaml`

**Navigation:**

- `src/` contains the service logic.
- `test/` contains code used for unittesting.
- `config/` contains configuration files used to run the service.
- `.env` contains environment variables.
