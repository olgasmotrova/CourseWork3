from project.dao.models.base import BaseMixin
from project.setup_db import db


class DirectorModel(BaseMixin, db.Model):
    __tablename__ = "director"
    name = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return f"<Director '{self.name.title()}'>"