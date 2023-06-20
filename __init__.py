from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "olámundo"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from views import my_blueprint
    from auth import autenticaçao

    app.register_blueprint(my_blueprint, url_prefix="/")
    app.register_blueprint(autenticaçao, url_prefix="/")

    from models import User,Post,Comment,Like

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists("blog_app/" + DB_NAME):
        with app.app_context():
            db.create_all()
            print("created database")