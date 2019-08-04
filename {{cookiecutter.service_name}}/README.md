## Overview

Describe your service functionality here.

## Development

**Test**

- Run `pytest`

**Run**

- Make sure you have `RabbitMQ` instance running using port `5672`
- Run `nameko run src.service --config config/nameko.yaml`

## Structure

- `src/` contains the service logic.
- `test/` contains code used for unit testing using `pytest`.
- `config/` contains configuration files used to run the service.
- `.env` contains environment variables.
