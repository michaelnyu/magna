run:
	python3 manage.py runserver 0:8000; \

install:
	pip3 install -r requirements.txt; \

migrate:
	python3 manage.py makemigrations; \
	python3 manage.py migrate; \