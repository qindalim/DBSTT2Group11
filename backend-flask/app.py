from flask import Flask, jsonify

from db import db

# ROUTES FOR RESOURCE
# from resources.user import blp as UserBlueprint
# from resources.item import blp as ItemBlueprint
# from resources.store import blp as StoreBlueprint
# from resources.tag import blp as TagBlueprint


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    api = Api(app)

    with app.app_context():
        import models  # noqa: F401
        db.create_all()

    return app
