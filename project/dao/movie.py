from sqlalchemy import desc
from project.dao.models import MovieModel
from project.config import BaseConfig


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, m_id: int):
        return self.session.query(MovieModel).filter(MovieModel.id == m_id).one_or_none()

    def get_all(self):
        return self.session.query(MovieModel).all()

    def get_all_by_status(self):
        return self.session.query(MovieModel).order_by(desc("year")).all()

    def get_all_by_page(self, page):
        return self.session.query(MovieModel).limit(
            BaseConfig.ITEMS_PER_PAGE).offset(
            BaseConfig.ITEMS_PER_PAGE * page -
            BaseConfig.ITEMS_PER_PAGE)

