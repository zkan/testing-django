# Testing Django

## Setting Up

```sh
python3 -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

## Running Django Server

```sh
cd testing_django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
