from project.dao import MovieDAO
from project.schemas.movie import MovieSchema
from project.exceptions import MovieNotFound


class MoviesService:
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_item_by_id(self, m_id: int):
        """
        Get movie by id
        """
        movie = self.movie_dao.get_by_id(m_id)
        if not movie:
            raise MovieNotFound
        return MovieSchema().dump(movie)

    def get_all_movies(self, filters):
        """
        Get all movies from base using 'pages'
        """

        if filters.get("page"):
            movies = self.movie_dao.get_all_by_page(filters["page"])
        elif filters.get("status") == "new":
            movies = self.movie_dao.get_all_by_status()
        else:
            movies = self.movie_dao.get_all()
        return MovieSchema(many=True).dump(movies)

