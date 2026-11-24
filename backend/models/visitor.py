
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from .company import Base


class Visitor(Base):

    __tablename__ = "visitors"

    id = Column(Integer, primary_key=True, autoincrement=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False
    )

    full_name = Column(String(150), nullable=False)

    mobile = Column(String(20), nullable=False)

    email = Column(String(150), nullable=True)

    visit_purpose = Column(String(255), nullable=False)

    device_type = Column(String(30), nullable=False)

    device_status = Column(
        String(30),
        default="not_enrolled"
    )

    visit_status = Column(
        String(30),
        default="registered"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
