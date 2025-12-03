from flask import Flask
from flask_admin import Admin
from flask import Blueprint, request, jsonify
from api.models import db, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity



api = Blueprint('api', __name__)

# -----------------------
# REGISTER USER
# -----------------------


@api.route('/register', methods=['POST'])
def register_user():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"msg": "Email y contraseña requeridos"}), 400

    # Check if user exists
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"msg": "Este email ya está registrado"}), 400

    # Create user
    new_user = User(email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "Usuario creado correctamente"}), 200


# -----------------------
# LOGIN USER
# -----------------------
@api.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({"msg": "Credenciales incorrectas"}), 401

    token = create_access_token(identity=user.id)

    return jsonify({"msg": "Login correcto", "token": token}), 200


# -----------------------
# PROTECTED EXAMPLE
# -----------------------
@api.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify(user.serialize()), 200
