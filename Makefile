test:
	poetry run coverage run -m pytest && poetry run coverage report

pc:
	poetry run pre-commit run --all-files

run:
	@python manage.py runserver

cs:
	@python manage.py collectstatic --noinput

mm:
	@python manage.py makemigrations

migrate:
	@python manage.py migrate

csu:
	@python manage.py createsuperuser

tw-watch:
	@./tailwindcss -i ./static/css/input.css -o ./static/css/styles.css --watch

requirements:
	@poetry export -f requirements.txt --output requirements.txt --without-hashes

gsk:
	@python ./manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
