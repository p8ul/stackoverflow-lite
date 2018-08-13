from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    with app.app_context():
        pass

    """ Basic Routes """

    # register our blueprints
    configure_blueprints(app)

    return app


def configure_blueprints(app):
    """Configure blueprints in views."""
    from app.questions.api.v1 import api
    from .home.views import home_blueprint

    for bp in [api, home_blueprint]:
        app.register_blueprint(bp)


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
