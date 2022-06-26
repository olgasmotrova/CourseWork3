from flask_restx import Resource, Namespace
from project.container import user_service
from flask import request
from flask_restx import abort
from project.utils import auth_required, get_id_from_token
from project.schemas.user import UserSchema
from project.exceptions import UserNotFound, TokensChangeFailed

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    @user_ns.response(200, 'OK')
    @user_ns.response(404, 'User not found')
    def get(self):
        try:
            token = request.headers['Authorization'].split('Bearer ')[-1]
            user_id = get_id_from_token(token)
            user = user_service.get_user_by_id(user_id)
            return UserSchema().dump(user)
        except UserNotFound:
            abort(404, message='User not found')

    @auth_required
    @user_ns.response(200, 'OK')
    @user_ns.response(404, 'User not found')
    def patch(self):
        try:
            token = request.headers['Authorization'].split('Bearer ')[-1]
            user_id = get_id_from_token(token)
            req_data = request.json
            req_data['id'] = user_id
            user_service.update_partial(req_data)
        except TokensChangeFailed:
            abort(404, message='Не получилось:(')
        return '', 200


@user_ns.route('/password/')
class UserChangePassword(Resource):
    @auth_required
    @user_ns.response(200, 'OK')
    @user_ns.response(404, 'User not found')
    def put(self):
        try:
            token = request.headers['Authorization'].split('Bearer ')[-1]
            user_id = get_id_from_token(token)
            req_data = request.json
            req_data['id'] = user_id
            user_service.update_password(req_data)
        except TokensChangeFailed:
            abort(400, message='Password not change')
        return 'Ok', 200










