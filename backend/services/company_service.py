import bcrypt

from database import SessionLocal
from models.company import Company
from models.user import User


def register_company(data):

    session = SessionLocal()

    try:
        # Check existing email
        existing_user = session.query(User).filter_by(
            email=data["email"]
        ).first()

        if existing_user:
            return False, "Email already registered"

        company = Company(
       company_name=data["company_name"],
       email=data["email"]
    )

        session.add(company)
        session.flush()

        # Hash password
        password_hash = bcrypt.hashpw(
            data["password"].encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        # Create company admin
        user = User(
            company_id=company.id,
            full_name=data["full_name"],
            email=data["email"],
            password_hash=password_hash,
            role="company_admin"
        )

        session.add(user)
        session.commit()

        return True, "Company registered successfully"

    except Exception as error:
        session.rollback()
        return False, str(error)

    finally:
        session.close()
         