from project.container import auth_service
from flask_restx import Resource, Namespace, abort
from flask import request, redirect
from project.exceptions import InvalidTokens, IncorrectData


auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class RegisterView(Resource):
    @auth_ns.response(201, 'user registered')
    @auth_ns.response(400, 'Bad request')
    def post(self):
        try:
            data = request.json
            auth_service.register(
                email= data['email'],
                password=data['password']
            )
            return redirect('/')
        except IncorrectData:
            abort(400, message='credentials error')


@auth_ns.route('/login/')
class LoginView(Resource):
    @auth_ns.response(201, 'Tokens created')
    @auth_ns.response(400, 'Bad request')
    def post(self):
        try:
            data = request.json
            tokens = auth_service.login(
                email=data['email'],
                password=data['password']
            )
            return tokens, 201
        except IncorrectData:
            abort(400, message='credentials error')

    @auth_ns.response(201, 'Tokens changed')
    @auth_ns.response(401, 'Invalid tokens')
    def put(self):
        try:
            refresh_token = request.json['refresh_token']
            return auth_service.update_tokens(refresh_token), 201
        except InvalidTokens:
            abort(401, message='Invalid tokens')

