startserver:
	pip install poetry
	poetry install
	poetry run python hexlet-code/manage.py migrate
	poetry run python hexlet-code/manage.py runserver 0.0.0.0:80
