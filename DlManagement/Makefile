.PHONY: install shell build down up makemigrations migrate createsuperuser

PYTHON = python3
MANAGE = $(PYTHON) manage.py
DOCKER = docker-compose

install:
	pip install poetry

shell:
	poetry shell

install-dependencies:
	poetry install

build:
	$(DOCKER) build

down:
	$(DOCKER) down

up: build
	$(DOCKER) up

makemigrations:
	$(MANAGE) makemigrations

migrate: makemigrations
	$(MANAGE) migrate

createsuperuser: migrate
	$(MANAGE) createsuperuser