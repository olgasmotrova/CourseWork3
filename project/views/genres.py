from project.container import genre_service
from flask_restx import Namespace, Resource, abort
from project.exceptions import GenreNotFound
from flask import request


genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    @genres_ns.response(200, 'OK')
    def get(self):
        try:
            page = request.args.get('page', type=int)
            filters = {'page': page}
            return genre_service.get_all_genres(filters)
        except GenreNotFound:
            abort(404, message='Genres not found')


@genres_ns.route('/<int:genre_id>')
class GenreView(Resource):
    @genres_ns.response(200, 'OK')
    @genres_ns.response(404, 'Genre not found')
    def get(self, genre_id: int):
        try:
            return genre_service.get_item_by_id(genre_id)
        except GenreNotFound:
            abort(404, message='Genre not found')
