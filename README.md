# Case Challenge

## Requirements:
### For running the project on a docker container:
* Docker
### For running the project on the terminal, a virual enviroment is recommended:
* Python3
* Virtualenv
* [pyenv](https://github.com/pyenv/pyenv)
* [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

## Instalation:
### For the docker container
#### Create a .env file like this for the container to run properly

```
  ENV='development'
  DB='db_case_challenge'
  TEST_DB='test_case_challenge'
  DB_USER='case_challenge'
  DB_HOST='db'
  DB_PASSWORD='case_challenge'
  DB_PORT='5432'
  WEB_SERVER_HOST="0.0.0.0"
  WEB_SERVER_PORT=8000
  WEB_SERVER_RELOAD= True
```
---

With the .env created, you just need to up the containers

```
  docker-compose build
  docker-compose up
```
On the first 'up' it is possible that the server might return an error, in that case, stop the running containers and start again using `docker-compose up`

### For running the project on the terminal (with auto-reload and for running tests)
With a python virtual enviroment set up, install the requirements
```
  make setup
```
Now create a .env file like this:
```
  ENV='development'
  DB='db_case_challenge'
  TEST_DB='test_case_challenge'
  DB_USER='case_challenge'
  DB_HOST='localhost'
  DB_PASSWORD='case_challenge'
  DB_PORT='5433'
  WEB_SERVER_HOST="localhost"
  WEB_SERVER_PORT=8000
  WEB_SERVER_RELOAD= True
```
then, use docker to run and create the databases for dev and testing
```
  docker-compose build
  docker-compose up
```
With the postgres container up, you can you can use `make run` to run the application, and access the docs in 'http://localhost:8000/docs#/'
To run tests, run `make test`
