test:
	poetry run coverage run -m pytest && poetry run coverage report

pc:
	poetry run pre-commit run --all-files
