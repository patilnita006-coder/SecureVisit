import bcrypt

from database import SessionLocal
from models.user import User
from flask_jwt_extended import create_access_token


def login_user(data):

    session = SessionLocal()

    try:
        user = session.query(User).filter_by(
            email=data["email"]
        ).first()

        if not user:
            return False, "Invalid email or password"

        if user.status != "active":
            return False, "Your account is inactive"

        password_valid = bcrypt.checkpw(
            data["password"].encode("utf-8"),
            user.password_hash.encode("utf-8")
        )

        if not password_valid:
            return False, "Invalid email or password"

        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={
                "company_id": user.company_id,
                "role": user.role
            }
        )

        return True, {
            "message": "Login successful",
            "access_token": access_token,
            "user": {
                "id": user.id,
                "company_id": user.company_id,
                "full_name": user.full_name,
                "email": user.email,
                "role": user.role
            }
        }

    except Exception as error:
        return False, str(error)

    finally:
        session.close()