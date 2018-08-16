### Fask create app

# Author: P8ul Kinuthia
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
    """Configure blueprints in views."""
    from app.questions.api.v1 import api
    from .home.views import home_blueprint
    from app.users.api.v1 import api as user_api

    for bp in [api, user_api, home_blueprint]:
        app.register_blueprint(bp)


def configure_extensions():
    db.test()


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
