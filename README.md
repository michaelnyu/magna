# Welcome to the Magna API

A backend API for Creative Lab's Liberty In North Korea Project

Check out **Creative Labs** at:
	uclacreatives.com

### A short guide to run:

#### Using Postgres

```
	** install postgres **
	psql
	>> CREATE DATABASE magna_db;
	>> CREATE USER admin WITH PASSWORD 'password123';
	>>ALTER ROLE admin SET client_encoding TO 'utf8';
	>>ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
	>>ALTER ROLE admin SET timezone TO 'UTC';
	>>GRANT ALL PRIVILEGES ON DATABASE magna_db TO admin;

```


#### Running the environment for the first time

```
	** clone repo **
	** install virtualenv if you have not already **
			** $ pip3 install virtual env **
	$ cd magna
	$ python3 -m venv env
	$ source env/bin/activate
	$ cd magna
	$ make install
	$ make migrate
	$ make test
	$ make dev
```


#### Running the environment subsequently

```
	$ make dev
```