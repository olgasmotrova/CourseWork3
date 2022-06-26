from project.dao.models import GenreModel
from project.config import BaseConfig


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, pk):
        return self.session.query(GenreModel).filter(GenreModel.id == pk).one_or_none()

    def get_all(self):
        return self.session.query(GenreModel).all()

    def get_all_by_page(self, page):
        return self.session.query(GenreModel).limit(
            BaseConfig.ITEMS_PER_PAGE).offset(
            BaseConfig.ITEMS_PER_PAGE * page -
            BaseConfig.ITEMS_PER_PAGE)
