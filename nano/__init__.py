from flask import Flask


def nano_blog():
    app = Flask(__name__)

    from .home.home import home_bp

    app.register_blueprint(blueprint=home_bp)

    return app
