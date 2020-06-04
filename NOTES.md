# Seku

| Lenguaje | Versión        |
| -------- | -------------- |
| Python   | Python 3.8.2   |

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
├── game
└── senku

## Migration
## Generate migrations
python manage.py makemigrations game

## Execute migraitons
python manage.py migrate

## Run server
python manage.py runserver
```

## Creating frontend
```bash
## Create a django app
django-admin startapp frontend

## Components folder
mkdir -p ./frontend/src/components

## Static files folder
mkdir -p ./frontend/{static,templates}/frontend

## Setup react, webpack and babel
cd ./frontend && npm init -y

## Install webpack
npm i webpack webpack-cli --save-dev

## Install babel
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev

## Install react
npm i react react-dom --save-dev

## Compile assets
npm run dev

## Run server
python manage.py runserver
```

## References

| Type          | Link                                                                                |
| ------------- | ----------------------------------------------------------------------------------- |
| Documentation | https://docs.djangoproject.com/en/3.0/                                              |
| Tutorial      | https://www.valentinog.com/blog/drf/#django-rest-with-react-creating-a-django-model |