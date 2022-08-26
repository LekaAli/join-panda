run:
	poetry run python ./api/manage.py runserver

createsuperuser:
	poetry run python ./api/manage.py createsuperuser

makemigrations:
	poetry run python ./api/manage.py makemigrations

migrate:
	poetry run python ./api/manage.py migrate

shell:
	poetry run python ./api/manage.py shell

install:
	poetry install

tests:
	poetry run ./api/manage.py tests