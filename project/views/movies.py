from flask_restx import Resource, Namespace, abort
from project.exceptions import MovieNotFound
from project.container import movie_service
from flask import request

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    @movies_ns.response(200, 'OK')
    def get(self):
        try:
            page = request.args.get('page', type=int)
            status = request.args.get('status')
            filters = {
                'status': status,
                'page': page
        }
            return movie_service.get_all_movies(filters)
        except MovieNotFound:
            abort(404, 'Movies not found')


@movies_ns.route('/<int:movie_id>/')
class MoviesView(Resource):
    @movies_ns.response(200, 'OK')
    @movies_ns.response(404, 'Movie not found')
    def get(self, movie_id: int):
        try:
            return movie_service.get_item_by_id(movie_id)
        except MovieNotFound:
            abort(404, message='Movie not found')

