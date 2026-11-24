from database import SessionLocal
from models.visitor import Visitor


def register_visitor(data, company_id):

    session = SessionLocal()

    try:
        visitor = Visitor(
            company_id=company_id,
            full_name=data["full_name"],
            mobile=data["mobile"],
            email=data.get("email"),
            visit_purpose=data["visit_purpose"],
            device_type=data["device_type"].lower()
        )

        session.add(visitor)
        session.commit()
        session.refresh(visitor)

        return True, {
            "message": "Visitor registered successfully",
            "visitor_id": visitor.id
        }

    except Exception as error:
        session.rollback()
        return False, str(error)

    finally:
        session.close()