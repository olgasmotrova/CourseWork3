from project.dao.director import DirectorDAO
from project.schemas.director import DirectorSchema
from project.exceptions import DirectorNotFound


class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_item_by_id(self, d_id):
        """
        Get director by id
        """
        director = self.director_dao.get_by_id(d_id)
        if not director:
            raise DirectorNotFound
        return DirectorSchema().dump(director)

    def get_all_directors(self, filters):
        """
        Get all directors using 'pages'
        """
        if filters.get("page"):
            directors = self.director_dao.get_all_by_page(filters.get("page"))
        else:
            directors = self.director_dao.get_all()
        return DirectorSchema(many=True).dump(directors)