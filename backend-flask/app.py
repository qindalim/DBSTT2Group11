from flask import Flask, jsonify
from flask_restful import Api

from db import db

# ROUTES FOR RESOURCE
# from resources.user import blp as UserBlueprint
# from resources.item import blp as ItemBlueprint
# from resources.store import blp as StoreBlueprint
# from resources.tag import blp as TagBlueprint


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
db.init_app(app)
api = Api(app)

if __name__ == "__main__":
    app.run(debug=True)

with app.app_context():
    import models  # noqa: F401
    db.create_all()



