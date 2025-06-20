from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User
from app.schemas.user_schema import UserSchema
from marshmallow import ValidationError

user_bp = Blueprint("user", __name__)
user_schema = UserSchema()
user_list_schema = UserSchema(many=True)
@user_bp.route("/create_user", methods=["POST"])
def create_user():
    print("HIT /create_user")
    data = request.get_json()
    try:
        user_data = user_schema.load(data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    
    new_user = User(**user_data)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(user_schema.dump(new_user)), 201


@user_bp.route("/get_users", methods=["GET"])
def list_people():
    users = User.query.all() 
    return jsonify(user_list_schema.dump(users))