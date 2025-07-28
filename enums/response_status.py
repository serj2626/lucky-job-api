from enum import Enum

class ResponseStatus(str, Enum):
    sent = "sent"                   # Отклик отправлен
    viewed = "viewed"               # Работодатель посмотрел
    rejected = "rejected"           # Отказ
    approved = "approved"           # Принят, продолжение общения
    interview = "interview"         # Приглашение на интервью