## Overview

Template for creating microservices using [nameko](https://www.nameko.io/).
Powered by [cookiecutter](https://github.com/cookiecutter/cookiecutter).

## Usage

Prerequisite:

- [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [pyenv](https://github.com/pyenv/pyenv)
- [pipenv](https://github.com/pypa/pipenv)

To start new project:

```
cookiecutter gh:pythonjokeun/nameko-template -f
```

## Structure

- `src/` contains the service logic.
- `test/` contains code used for unit testing using `pytest`.
- `config/` contains configuration files used to run the service.
