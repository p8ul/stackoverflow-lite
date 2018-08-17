# Flask create app

# Author: P8ul
# https://github.com/p8ul

from flask import Flask
from .migrations.db import db


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    with app.app_context():
        pass

    """ Basic Routes """

    # register our blueprints
    configure_blueprints(app)

    # register extensions
    configure_extensions()

    return app


def configure_blueprints(app):
    """Configure blueprints ."""
    from app.questions.api.v1.view import question_blueprint
    from .home.views import home_blueprint
    from .auth.api.v1.view import auth_blueprint
    from .answers.api.v1.view import answers_blueprint
    from .votes.api.v1.view import votes_blueprint
    from .comments.api.v1.view import comments_blueprint

    app_blueprints = [
        answers_blueprint,
        question_blueprint,
        auth_blueprint,
        votes_blueprint,
        comments_blueprint,
        home_blueprint
    ]

    for bp in app_blueprints:
        app.register_blueprint(bp)


def configure_extensions():
    db.test()


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
