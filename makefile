PROJECT_NAME=hackernews

# Common

all: run

run:
	@docker-compose up

stop:
	@docker-compose stop

down:
	@docker-compose down

migrations:
	@docker exec -it hackernews alembic revision --autogenerate;

migrate:
	@docker exec -it hackernews alembic upgrade head;

psql:
	@docker exec -it hackernews_postgres psql -U postgres