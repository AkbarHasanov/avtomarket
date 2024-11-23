from flask import Blueprint, jsonify, request
from bot.database.session import SessionLocal
from bot.models.user import User

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/click/prepare', methods=['POST'])
def prepare():
    db = SessionLocal()
    users = db.query(User).all()
    return jsonify([{"id": user.id, "username": user.username, "chat_id": user.chat_id} for user in users])


@api_blueprint.route('/click/complete', methods=['POST'])
def complete():
    db = SessionLocal()
    data = request.json
    if not data.get('username') or not data.get('chat_id'):
        return jsonify({"error": "Invalid input"}), 400

    user = User(username=data['username'], chat_id=data['chat_id'])
    db.add(user)
    db.commit()
    return jsonify({"message": "User added", "user": {"id": user.id, "username": user.username}}), 201
