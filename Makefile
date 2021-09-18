# Makefile for command shortcuts

start:
	python manage.py runserver

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

admin:
	python manage.py createsuperuser

