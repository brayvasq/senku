# Seku

https://www.valentinog.com/blog/drf/#django-rest-with-react-creating-a-django-model

## Creating project
```bash
## Installing dependencies
pip install django djangorestframework

## Creating django project
django-admin startproject senku .

## Creating a django app
django-admin startapp game

## Folder structure
tree -d -L 1
.
├── bin
├── game
├── lib
└── senku

## Migration
## Generate migrations
python manage.py makemigrations game

## Execute migraitons
python manage.py migrate

## Run server
python manage.py runserver
```