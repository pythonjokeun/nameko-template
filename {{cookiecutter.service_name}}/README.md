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

**Navigation:**

- `src/` contains the service logic.
- `test/` contains code used for unittesting.
- `config/` contains configuration files used to run the service.
- `.env` contains environment variables.
