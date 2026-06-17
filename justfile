# dev:
#     uv run fastapi dev

dev:
    python3 cookbook/main.py

format:
    ruff format

lint:
    ruff check --fix