from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt

from schemas.visitor_schema import validate_visitor_data
from services.visitor_service import register_visitor

visitor_bp = Blueprint("visitor", __name__)


@visitor_bp.route("/register", methods=["POST"])
@jwt_required()
def register():

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "Request data is required"
        }), 400

    is_valid, message = validate_visitor_data(data)

    if not is_valid:
        return jsonify({
            "status": "error",
            "message": message
        }), 400

    claims = get_jwt()

    if claims.get("role") != "company_admin":
        return jsonify({
            "status": "error",
            "message": "Access denied"
        }), 403

    company_id = claims.get("company_id")

    success, result = register_visitor(data, company_id)

    if not success:
        return jsonify({
            "status": "error",
            "message": result
        }), 400

    return jsonify({
        "status": "success",
        "data": result
    }), 201