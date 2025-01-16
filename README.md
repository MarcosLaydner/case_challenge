# Case Challenge

## Requirements:
### For running the project on a docker container:
* Docker
### For running the project on the terminal, a virual enviroment is recommended:
* Python3.11
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

## Known problems / Shortcomings (Things I would improve in a real scenario/ given more time):
1. While I created different layers with their own responsabilities, I feel like the repositories could use more abstraction, like creating an interface to be implemented by the respective repositories. This would make changing orms easier, and better decouple the databse layer with the application layer.
2. The same applies for the test factories, which are coupled to the created repositories for the sake of time.
3. The docker setup could be improve to remove the need to sometimes have to stop it then up again to work propperly.
4. The application could use an activate route, that would reactivate accounts that have been previously deactivated.
5. The application could use a validator for email. I did not implemented it as I saw it wasn't critical to any required functionality of the API, but in a real scenario it would be necessary.
6. I opted to not have emails be unique as I also saw this as not critical.

