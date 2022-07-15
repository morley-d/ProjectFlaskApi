from unittest.mock import MagicMock
import pytest

from app.dao.model.user import User
from app.dao.user import UserDAO
from app.services.user import UserService


@pytest.fixture()
def user_dao():
    user_dao = UserDAO(None)

    john = User(id=1, name='john')
    kate = User(id=2, name='kate')
    max = User(id=3, name='max')

    user_dao.get_one = MagicMock(return_value=john)
    user_dao.get_all = MagicMock(return_value=[john, kate, max])
    user_dao.create = MagicMock(return_value=User(id=3))
    user_dao.update = MagicMock()
    user_dao.delete = MagicMock()

    return user_dao


class TestUserService:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        self.user_service = UserService(dao=user_dao)

    def test_get_one(self):
        user = self.user_service.get_one(1)
        assert user is not None
        assert user.id is not None

    def test_get_all(self):
        users = self.user_service.get_all()
        assert len(users) > 0

    def test_create(self):
        user_d = {
            "name": "Ivan",
            "age": 36
        }
        user = self.user_service.create(user_d)
        assert user.id is not None

    def test_update(self):
        user_d = {
            "id": 4,
            "name": "Ivan",
            "age": 36
        }
        self.user_service.update(user_d)

    def test_delete(self):
        self.user_service.delete()
