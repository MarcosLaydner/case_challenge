run:
	python case_challenge/main.py

test:
	pytest -vv

setup:
	pip install -r requirements.txt

# Initialize your local database
psql-up: 
	docker compose -f .docker/docker-compose.yml up -d --build --force-recreate --remove-orphans db
# Remove your local database
psql-down: 
	docker-compose -f .docker/docker-compose.yml down -v --remove-orphans