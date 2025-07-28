# ⚙️ Переменные
APP_DIR=app
ENV_FILE=.env

# 📦 Установка зависимостей
install:
	pip install -r requirements.txt

# ✅ Форматирование кода
fmt:
	autoflake --remove-all-unused-imports --remove-unused-variables --in-place -r $(APP_DIR)
	isort $(APP_DIR)
	black $(APP_DIR)

# ✅ Проверка качества кода
check:
	isort --check-only $(APP_DIR)
	black --check $(APP_DIR)

# 🧪 Запуск тестов (если есть pytest)
test:
	pytest -v

# 🐘 Миграции
migrate:
	alembic upgrade head

# 🧬 Создание миграции
makemigrations:
	alembic revision --autogenerate -m "Auto migration"

# 🚀 Запуск dev-сервера
dev:
	uvicorn $(APP_DIR).main:app --reload --host 0.0.0.0 --port 8000

# 🐳 Запуск Docker
up:
	docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -f

# 🧼 Очистка build-ов
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +




# Как использовать
# bash
# Копировать
# Редактировать
# make fmt         # автоформат
# make check       # проверка стиля
# make dev         # локальный запуск FastAPI
# make up          # docker-compose up
# make migrate     # alembic upgrade