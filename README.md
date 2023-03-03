# Library Manager

## Install dependencies

```bash
poetry install
```

## Init DB (Migrate)

```bash
poetry run python ./manage.py migrate
```

## Create super user (admin)

```bash
poetry run python ./manage.py createsuperuser
```

## Run server

```bash
poetry run python ./manage.py runserver
```

## Format code

```bash
poetry run black $(git ls-files '*.py')
poetry run isort $(git ls-files '*.py')
```
