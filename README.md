# todo-list-fastapi
A simple todolist api project that deploys adminer, postgres, and fastapi in separate docker containers.

## Run
```
docker-compose up
```

## Migrations
- Make your changes in the models.
- Start the project using `docker-compose up --build -d`
- Wait for the containers to go online.
- Open a shell in the todolist container using `docker-compose exec todolist bash`
- Run the following to make changes `alembic revision --autogenerate -m "Revision Message"`
- exit the shell and run `docker-compose down`

Next time you build the project, `alembic upgrade head` in docker-entrypoint.sh will make the relevant changes in the database.
