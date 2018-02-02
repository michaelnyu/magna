build:
	docker-compose build

devup:
	docker-compose up

devdown:
	docker-compose down

env:
	source api/bin/activate; \

envdown:
	deactivate; \

install:
	pip3 install -r requirements.txt; \
	pip3 install djangorestframework; \