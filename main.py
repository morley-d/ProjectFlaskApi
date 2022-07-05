from flask import Flask
from flask_restx import Api

from app.config import Config
from app.dao.model.user import User
from app.database import db
from app.views.auth import auth_ns
from app.views.users import user_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    configure_app(application)
    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    load_data()


def load_data():
    user = User(username="root", password="random_pass", role="admin")
    db.create_all()
    with db.session.begin():
        db.session.add_all([user])


app = create_app(Config())

if __name__ == '__main__':
    app.run(host="localhost", port=5055, debug=True)
