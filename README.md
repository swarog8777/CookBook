# Настройка проекта CookBook

Клонирование репозитория
```bash
git clone git@github.com:swarog8777/CookBook.git
```
Открыть проект и в корне создать .env
```
POSTGRES_USER=user
POSTGRES_PASSWORD=1234
POSTGRES_DB=cookbookdb
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

Запуск Postgres
```bash
docker compose -f "docker-compose.dev.yml" up -d
```
Миграции
```bash
alembic upgrade head
```

RUN
```bash
uv install
uv run fastapi dev
```

RUFF JUST
