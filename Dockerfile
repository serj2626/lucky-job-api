# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
# COPY pyproject.toml poetry.lock* requirements.txt* ./
COPY pyproject.toml  requirements.txt* ./

# Устанавливаем зависимости
# Если используешь poetry:
# RUN pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
# Если requirements.txt:
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь проект
COPY . .

# Копируем и даём права скрипту
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Указываем порт (если нужно)
EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]