
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class Company(Base):

    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, autoincrement=True)

    company_name = Column(String(150), nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    phone = Column(String(20), nullable=True)

    address = Column(String(255), nullable=True)

    status = Column(String(20), default="active")

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

