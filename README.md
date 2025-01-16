# Case Challenge
## Time taken ~5 hours
- ~2 hours for project setup (docker containers, installation, fastapi server setup)
- ~2 hours on the required functionalty and project structure
- ~1 hour for the tests

## Implementation notes:
The idea was to implement the aplication in a clean manner, keep it organized, layered and as decoupled as possible, while at the same time trying to not overengineer anything due to both the time constraint and simplicity of the task.
So the application has 4 layers with their own responsabilities:

  1. Controllers receive the requests and direct them to the proper use cases to be resolved, returning the necessary information when necessary
  2. Models handle the transport and validation of data through the layers
  3. Use cases contain the necessary logic of the application, acting not only as a bridge from the controllers to the orm, as holders of the business logic
  4. Repositories handle teh communication with the ORM, requesting necessary calls to the database

The file structure is divided in domains, with all related files organized withing their domains


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
4. I could have added a layer of serializers for incoming and outgoing data for the controllers, to have better control of data coming in and out of the application, but opted not due to the time constraint and simplicity of the project
5. The application could use an activate route, that would reactivate accounts that have been previously deactivated.
6. The application could use a validator for email. I did not implemented it as I saw it wasn't critical to any required functionality of the API, but in a real scenario it would be necessary.
7. I opted to not have emails be unique as I also saw this as not critical.

