from project.dao.models.user import UserModel


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_user_by_id(self, uid: int):
        user = self.session.query(UserModel).filter(UserModel.id == uid).one_or_none()
        return user

    def update(self, user_data):
        self.session.add(user_data)
        self.session.commit()

