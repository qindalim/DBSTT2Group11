from db import db

class UserModel(db.Model):
    __tablename__ = "User"

    EmployeeID = db.Column(db.Integer, primary_key=True, unique=True)
    Password = db.Column(db.String(20), nullable=False)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    Age = db.Column(db.Integer, nullable=False)

    policies = db.relationship(
        "PolicyModel",
        back_populates="User",
        cascade="all, delete",
        passive_deletes=True,
    )    

    def __repr__(self):
        return f"Policy(EmployeeID = {EmployeeID}, Password = {Password},\
                FirstName = {FirstName}, LastName = {LastName},\
                Age = {Age})"