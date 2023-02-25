from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Api

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost:3306/insurancedata"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
CORS(app)

db = SQLAlchemy(app)
# db.init_app(app)
# api = Api(app)



class UserModel(db.Model):
    __tablename__ = "User"

    EmployeeID = db.Column(db.Integer, primary_key=True, unique=True)
    Password = db.Column(db.String(20), nullable=False)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    Age = db.Column(db.Integer, nullable=False)

    # policies = db.relationship(
    #     "PolicyModel",
    #     back_populates="User",
    #     cascade="all, delete",
    #     passive_deletes=True,
    # )    

    # def __repr__(self):
    #     return f"Policy(EmployeeID = {EmployeeID}, Password = {Password},\
    #             FirstName = {FirstName}, LastName = {LastName},\
    #             Age = {Age})"



class PolicyModel(db.Model):
    __tablename__ = "InsurancePolicies"

    InsuranceID = db.Column(db.Integer, primary_key=True)
    EmployeeID = db.Column(db.Integer, 
                           db.ForeignKey("User.EmployeeID", ondelete="CASCADE"), 
                           nullable=False)
    InsuranceType = db.Column(db.String(100), nullable=False)
    PolicyStartDate = db.Column(db.String(255), nullable=False)
    PolicyTerm = db.Column(db.String(100), nullable=False)
    PolicyEndDate = db.Column(db.String(255), nullable=False)
    ClaimLimit = db.Column(db.Float(precision=2), nullable=False)
    RemainingClaimLimit = db.Column(db.Float(precision=2), nullable=False)

    # users = db.relationship("UserModel", back_populates="policies")
    # claims = db.relationship(
    #     "ClaimsModel",
    #     back_populates="InsurancePolicies",
    #     cascade="all, delete",
    #     passive_deletes=True,
    # )    

    def __repr__(self):
        return f"Policy(InsuranceID = {InsuranceID}, EmployeeID = {EmployeeID},\
                InsuranceType = {InsuranceType}, PolicyStartDate = {PolicyStartDate},\
                PolicyTerm = {PolicyTerm}, PolicyEndDate = {PolicyEndDate},\
                ClaimLimit = {ClaimLimit}, RemainingClaimLimit = {RemainingClaimLimit})"

    

class ClaimsModel(db.Model):
    __tablename__ = "InsuranceClaims"

    ClaimID = db.Column(db.Integer, primary_key=True, nullable=False)
    InsuranceID = db.Column(db.Integer,  
                            db.ForeignKey("InsurancePolicies.InsuranceID", ondelete="CASCADE"), 
                            primary_key=True, 
                            nullable=False)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    ExpenseDate = db.Column(db.String(255), nullable=False)
    Amount = db.Column(db.Float(precision=2), nullable=False)
    Purpose = db.Column(db.String(255), nullable=False)
    FollowUp = db.Column(db.Boolean, nullable=False)
    PreviousClaimID = db.Column(db.Integer, nullable=False)
    Status = db.Column(db.String(20), nullable=False)
    LastEditedClaimDate = db.Column(db.String(255), nullable=False)

    # policies = db.relationship("PolicyModel", back_populates="claims")

    def __repr__(self):
        return f"Policy(ClaimID = {ClaimID}, InsuranceID = {InsuranceID},\
                FirstName = {FirstName}, LastName = {LastName},\
                ExpenseDate = {ExpenseDate}, Amount = {Amount},\
                Purpose = {Purpose}, FollowUp = {FollowUp},\
                PreviousClaimID = {PreviousClaimID}, Status = {Status},\
                LastEditedClaimDate = {LastEditedClaimDate})"


@app.route("/test")
def test():
    test_user = UserModel.query.first()
    return str(test_user.EmployeeID)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)

