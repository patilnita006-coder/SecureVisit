import os
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from flask import Flask, jsonify
from controllers.auth_controller import auth_bp
from flask_cors import CORS
from controllers.company_controller import company_bp
from controllers.visitor_controller import visitor_bp
load_dotenv()
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)
CORS(app)
app.register_blueprint(company_bp, url_prefix="/api/companies")
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(visitor_bp, url_prefix="/api/visitors")
@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "SecureVisit API is running!",
        "project": "SecureVisit"
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "backend": "running"
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
