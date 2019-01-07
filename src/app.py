from flask import Flask
from src import db


def create_app(config=None):
    app = Flask(__name__)
    if config is not None:
        app.config.from_object(config)

    db.init_app(app)


    from src.blueprint.catalog.routes import main_blueprint
    app.register_blueprint(main_blueprint)


    return app

