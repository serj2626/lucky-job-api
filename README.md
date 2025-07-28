# 🧠 Lucky Job — Платформа для поиска работы программистами

Lucky Job — это современная платформа, которая объединяет разработчиков и IT-компании. Система поддерживает real-time общение через WebSocket, уведомления, новостную ленту, фильтрацию вакансий и профилей, а также мощную админку для компаний и HR.

## Проект на стадии разработки 🚧

📂 Структура проекта

app/
│
├── main.py                     # точка входа (FastAPI instance)
├── deps.py                     # зависимости (get_db, current_user и т.п.)
├── core/                       # конфиги, jwt, security, settings
│   ├── config.py
│   ├── security.py
│   └── jwt.py
│
├── models/                     # SQLAlchemy модели
│   └── user.py
│
├── schemas/                    # Pydantic схемы
│   └── user.py
│
├── enums/                      # Enum-ы (UserRole, статус вакансии и т.п.)
│   └── user_role.py
│
├── services/                   # бизнес-логика (email, celery tasks, elastic)
│   └── user_service.py
│
├── use_cases/                 # "юнит" логики для API — use-case подход
│   └── user_create.py
│
├── api/                        # маршруты
│   ├── deps.py                 # зависимости
│   ├── v1/
│   │   ├── user.py
│   │   ├── auth.py
│   │   └── ...
│   └── router.py               # include всех роутов
│
├── db/
│   ├── session.py              # SessionLocal, engine
│   └── base.py                 # Base = declarative_base()
│
├── tasks/                      # celery background tasks
│   └── send_email.py
│
└── tests/                      # pytest / httpx
    └── ...
