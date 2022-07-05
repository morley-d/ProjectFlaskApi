from app.dao.user import UserDAO
from app.database import db
from app.services.auth import AuthService
from app.services.user import UserService

user_dao = UserDAO(db.session)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service)
