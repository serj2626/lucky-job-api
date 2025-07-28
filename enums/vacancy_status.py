from enum import Enum


class VacancyStatus(str, Enum):
    draft = "draft"  # Черновик, не опубликовано
    published = "published"  # Видна всем
    closed = "closed"  # Закрыта, неактуальна
    archived = "archived"  # Удалена/спрятана


# from sqlalchemy import Enum as SQLEnum
# from sqlalchemy.orm import Mapped, mapped_column
# from app.enums.vacancy_status import VacancyStatus

# status: Mapped[VacancyStatus] = mapped_column(SQLEnum(VacancyStatus), 
# default=VacancyStatus.draft)
