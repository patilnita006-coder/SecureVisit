from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from .company import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, autoincrement=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False
    )

    visitor_id = Column(
        Integer,
        ForeignKey("visitors.id"),
        nullable=False
    )

    device_type = Column(String(30), nullable=False)

    device_id = Column(String(255), nullable=True)

    management_status = Column(
        String(30),
        default="not_enrolled"
    )

    camera_status = Column(
        String(30),
        default="not_verified"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )