from flask import Flask, jsonify
from .migrations.db import db


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    with app.app_context():
        pass

    # register our blueprints
    configure_blueprints(app)

    # register extensions
    configure_extensions()

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify("The resource does not exist"), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify("Encountering an internal error with our server!"), 500

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify("You do not permission to access this resource"), 403

    return app


def configure_blueprints(app):
    """ Configure blueprints . """
    from .api.v2.questions.routes import question_blueprint
    from .home.views import home_blueprint
    from .api.v2.auth.routes import auth_blueprint
    from .api.v2.answers.routes import answers_blueprint
    from .api.v2.votes.routes import votes_blueprint
    from .api.v2.comments.routes import comments_blueprint
    from .api.v2.users.routes import users_blueprint

    app_blueprints = [
        answers_blueprint,
        question_blueprint,
        auth_blueprint,
        votes_blueprint,
        comments_blueprint,
        home_blueprint,
        users_blueprint
    ]

    for bp in app_blueprints:
        app.register_blueprint(bp)


def configure_extensions():
    db.migrate()


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
