from project.dao.models.base import BaseMixin
from project.setup_db import db


class GenreModel(BaseMixin, db.Model):
    __tablename__ = "genre"

    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Genre '{self.name.title()}'>"



