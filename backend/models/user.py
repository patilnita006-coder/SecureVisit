
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from .company import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=True
    )

    full_name = Column(String(150), nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    role = Column(String(30), default="company_admin")

    status = Column(String(20), default="active")

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

