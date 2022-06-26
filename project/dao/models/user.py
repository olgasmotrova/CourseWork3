from project.setup_db import db
from project.dao.models.base import BaseMixin


class UserModel(BaseMixin, db.Model):
    __tablename__ = "user"

    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favorite_genre = db.Column(db.Integer, db.ForeignKey("genre.id"))

    genre = db.relationship("GenreModel")

    def __repr__(self):
        return f"<User '{self.email.title()}'"