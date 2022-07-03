from flask import request
from flask_restx import Namespace, Resource
from marshmallow import Schema, fields

from app.container import user_service

user_ns = Namespace("users")


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        users = user_service.get_all()
        response = UserSchema(many=True).dump(users)
        return response, 200

    def post(self):
        data = request.json
        user = user_service.create(data)
        return "", 201, {"location": f"users/{user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def delete(self, uid):
        user_service.delete(uid)
        return "", 204
