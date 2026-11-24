from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from schemas.auth_schema import validate_login_data
from services.auth_service import login_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "Request data is required"
        }), 400

    is_valid, message = validate_login_data(data)

    if not is_valid:
        return jsonify({
            "status": "error",
            "message": message
        }), 400

    success, result = login_user(data)

    if not success:
        return jsonify({
            "status": "error",
            "message": result
        }), 401

    return jsonify({
        "status": "success",
        "data": result
    }), 200
@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():

    user_id = get_jwt_identity()
    claims = get_jwt()

    return jsonify({
        "status": "success",
        "message": "Token verified successfully",
        "user_id": user_id,
        "company_id": claims["company_id"],
        "role": claims["role"]
    }), 200