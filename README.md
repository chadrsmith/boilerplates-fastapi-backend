# FastAPI Backend Boilerplate
___
Boilerplate for a FastAPI application

## Authors
[Chad Smith](https://github.com/chadrsmith)

## Prerequisites
___
- `Python 3.12` installed on system
- Install `poetry` on system

## Getting Started
___
### Create .env file
Create a `.env` file in the root of the project directory. You will want to add the following variables:

```bash
APP_NAME="BOILERPLATE APP"
APP_VERSION="1.0.0"
APP_ENVIRONMENT="development"
PORT="3001"
```

### Install Dependencies
you will need to install the project dependencies found in the `pyproject.toml`.

```bash
poetry install
```

## Project Scripts
___
### Start App
Starts the application on the port defined in your `.env`
```bash
poetry run start
```

### Run Integration Tests
```bash
poetry run tests:integration
```

### Run Unit Tests
```bash
poetry run tests:unit
```
