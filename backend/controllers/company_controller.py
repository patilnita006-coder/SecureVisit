from flask import Blueprint, request, jsonify

from schemas.company_schema import validate_company_data
from services.company_service import register_company

company_bp = Blueprint("company", __name__)


@company_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "Request data is required"
        }), 400

    is_valid, message = validate_company_data(data)

    if not is_valid:
        return jsonify({
            "status": "error",
            "message": message
        }), 400

    success, message = register_company(data)

    if not success:
        return jsonify({
            "status": "error",
            "message": message
        }), 400

    return jsonify({
        "status": "success",
        "message": message
    }), 201