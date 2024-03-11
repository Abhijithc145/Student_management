SHELL := /bin/bash

env-setup:
	rm -rf venv
	python3 -m venv venv; \
	source venv/bin/activate; \
	pip install -r requirements.txt


run-local:
	source venv/bin/activate; \
	export CONFIG_PATH=common/configs/local.cfg; \
	python3 manage.py makemigrations; \
	python3 manage.py migrate; \
	black .; \
	python3 manage.py runserver 8000