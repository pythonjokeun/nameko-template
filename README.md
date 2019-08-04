## Overview

Template for creating microservices using [nameko](https://www.nameko.io/).
Powered by [cookiecutter](https://github.com/cookiecutter/cookiecutter).

## Usage

```
pip install cookiecutter
cookiecutter gh:pythonjokeun/nameko-template -f
```

## Structure

- `src/` contains the service logic.
- `test/` contains code used for unit testing using `pytest`.
- `config/` contains configuration files used to run the service.
- `.env` contains environment variables.
