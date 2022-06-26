from project.setup_db import db

from project.dao.genre import GenreDAO
from project.dao.director import DirectorDAO
from project.dao.movie import MovieDAO
from project.dao.user import UserDAO
from project.dao.auth import AuthDAO


from project.services.genres_service import GenresService
from project.services.directors_service import DirectorService
from project.services.movies_service import MoviesService
from project.services.user_service import UserService
from project.services.auth_service import AuthService


genre_dao = GenreDAO(session=db.session)
director_dao = DirectorDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)
auth_dao = AuthDAO(session=db.session)

genre_service = GenresService(genre_dao=genre_dao)
director_service = DirectorService(director_dao=director_dao)
movie_service = MoviesService(movie_dao=movie_dao)
user_service = UserService(user_dao=user_dao)
auth_service = AuthService(auth_dao=auth_dao)
