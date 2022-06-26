from project.dao.models import DirectorModel
from project.config import BaseConfig


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, d_id):
        return self.session.query(DirectorModel).filter(DirectorModel.id == d_id).one_or_none()

    def get_all(self):
        return self.session.query(DirectorModel).all()

    def get_all_by_page(self, page):
        return self.session.query(DirectorModel).limit(
            BaseConfig.ITEMS_PER_PAGE).offset(
            BaseConfig.ITEMS_PER_PAGE * page -
            BaseConfig.ITEMS_PER_PAGE)
