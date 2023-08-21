from flask import request, jsonify
from werkzeug.security import generate_password_hash
from app import app, db 
from models import User, Note 
from flask_jwt_extended import create_access_token

from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity


@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"success": False, "message": "缺少用户名或密码"}), 400

    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"success": False, "message": "用户名已存在"}), 400

    user = User(username=username, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    # return 1
    print("注册成功")
    return jsonify({"success": True, "message": "注册成功"}), 201

from werkzeug.security import check_password_hash

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"success": False, "message": "用户名或密码错误"}), 400

    access_token = create_access_token(identity=username)
    # 在这个示例中，我们简单地返回用户的用户名。
    
    return jsonify(access_token=access_token), 200


@app.route('/notes', methods=['GET'])
@jwt_required()  
def get_notes():
    notes = Note.query.all()
    return jsonify({"notes": [{"id": note.id, "username": note.username, "content": note.content} for note in notes]}), 200



@app.route('/notes', methods=['POST'])
@jwt_required()
def create_note():
    username = get_jwt_identity()
    content = request.json.get('content')
    # 你可能还想获取用户的ID并将其与便签关联。

    note = Note(content=content, username=username)
    db.session.add(note)
    db.session.commit()

    return jsonify({"success": True, "message": "便签创建成功"}), 201

@app.route('/notes/<int:note_id>', methods=['PUT'])
@jwt_required()
def update_note(note_id):
    content = request.json.get('content')
    note = Note.query.get(note_id)
    if not note:
        return jsonify({"success": False, "message": "便签未找到"}), 404

    note.content = content
    db.session.commit()

    return jsonify({"success": True, "message": "便签更新成功"}), 200

@app.route('/notes/<int:note_id>', methods=['DELETE'])
@jwt_required()
def delete_note(note_id):
    note = Note.query.get(note_id)
    if not note:
        return jsonify({"success": False, "message": "便签未找到"}), 404

    db.session.delete(note)
    db.session.commit()

    return jsonify({"success": True, "message": "便签删除成功"}), 200



