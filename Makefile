start:
	python manage.py runserver --noreload

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

admin:
	python manage.py createsuperuser

