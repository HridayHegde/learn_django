# Django Cheat Sheet
``` django-admin startproject mysite ``` Setup Starter Project

``` python manage.py startapp name ``` Setup App called *name*

``` python manage.py runserver ``` Run the server

``` python manage.py migrate ``` To initialize database or to commit changes to structure

``` python manage.py makemigrations polls ``` To make Models

``` python manage.py sqlmigrate polls 0001 ``` To check Models

``` python manage.py shell ``` To access the django ORM shell

``` python manage.py createsuperuser ``` Create Admin

``` {% url 'detail' question.id %} ``` Can be used to assign dynamic urls

``` self.assertIs() ``` Testing

``` {% load static %} ``` to load assets folder

``` {% static 'polls/style.css' %} ``` Sample asset access

``` https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c ``` For REST API

``` class HeroSerializer(serializers.HyperlinkedModelSerializer): class Meta: model = Hero fields = ('name', 'alias') ``` Basic Serializer