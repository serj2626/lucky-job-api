import uuid

from sqlalchemy.ext.declarative import declarative_base, declared_attr

DeclarativeBase = declarative_base()
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    @declared_attr.directive
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"
