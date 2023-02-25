from db import db


class UserModel(db.Model):
    __tablename__ = "user"

    employeeId = db.Column(db.Integer, primary_key=True, unique=True)
    password = db.Column(db.String(20), nullable=False)
    firstName = db.Column(db.String(50), nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    # employee = relationship("")


