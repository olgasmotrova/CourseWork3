from project.schemas.user import UserSchema
from project.dao.models import UserModel


class AuthDAO:
    def __init__(self, session):
        self.session = session

    def create(self, email: str, password: str) -> UserSchema:
        new_user = UserModel(
            email=email,
            password=password
        )
        self.session.add(new_user)
        self.session.commit()
        return UserSchema().dump(new_user)

    def get_user_by_email(self, email: str) -> UserSchema:
        user = self.session.query(UserModel).filter(UserModel.email == email).one_or_none()
        if user is not None:
            return UserSchema().dump(user)
        return None



