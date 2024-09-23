from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

db = SQLAlchemy()  # handles database
bcrypt = Bcrypt()  # handles encyption of password
login_manager = LoginManager()  # handles login session management
login_manager.login_view = 'users.login'  # if @login_required then give function name to redirect
login_manager.login_message_category = "info"  # which type of @login_required message class you want (here, used bootstrap class)

# Flask-Mail config
mail = Mail()


def create_app(config_class=config):
    # create flask app.
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # register modules.
    from flaskblog.users.routs import users
    from flaskblog.posts.routs import posts
    from flaskblog.main.routs import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    # for db creation(if not created) at run time.
    app.app_context().push()
    db.create_all()

    return app
