from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Api
from sqlalchemy import and_


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password0403@localhost:3306/insurancedata"
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

    def __init__(self, EmployeeID, Password, FirstName, LastName, Age):
        self.EmployeeID = EmployeeID
        self.Password = Password
        self.FirstName = FirstName
        self.LastName = LastName
        self.Age = Age


    def json(self):
        return {"EmployeeID": self.EmployeeID, "Password": self.Password, "FirstName": self.FirstName, "LastName": self.LastName, "Age": self.Age}

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

    def __init__(self, InsuranceID, EmployeeID, InsuranceType, PolicyStartDate, PolicyTerm, PolicyEndDate, ClaimLimit, RemainingClaimLimit):
        self.InsuranceID = InsuranceID
        self.EmployeeID = EmployeeID
        self.InsuranceType = InsuranceType
        self.PolicyStartDate = PolicyStartDate
        self.PolicyTerm = PolicyTerm
        self.PolicyEndDate = PolicyEndDate
        self.ClaimLimit = ClaimLimit
        self.RemainingClaimLimit = RemainingClaimLimit

    def json(self):
        return {"InsuranceID": self.InsuranceID, "EmployeeID": self.EmployeeID, "InsuranceType": self.InsuranceType, "PolicyStartDate": self.PolicyStartDate, "PolicyTerm": self.PolicyTerm, "PolicyEndDate": self.PolicyEndDate, "ClaimLimit": self.ClaimLimit, "RemainingClaimLimit": self.RemainingClaimLimit}

    # users = db.relationship("UserModel", back_populates="policies")
    # claims = db.relationship(
    #     "ClaimsModel",
    #     back_populates="InsurancePolicies",
    #     cascade="all, delete",
    #     passive_deletes=True,
    # )    

    # def __repr__(self):
    #     return f"Policy(InsuranceID = {InsuranceID}, EmployeeID = {EmployeeID},\
    #             InsuranceType = {InsuranceType}, PolicyStartDate = {PolicyStartDate},\
    #             PolicyTerm = {PolicyTerm}, PolicyEndDate = {PolicyEndDate},\
    #             ClaimLimit = {ClaimLimit}, RemainingClaimLimit = {RemainingClaimLimit})"

    

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

    def __init__(self, ClaimID, InsuranceID, FirstName, LastName, ExpenseDate, Amount, Purpose, FollowUp, PreviousClaimID, Status, LastEditedClaimDate):
        self.ClaimID = ClaimID
        self.InsuranceID = InsuranceID
        self.FirstName = FirstName
        self.LastName = LastName
        self.ExpenseDate = ExpenseDate
        self.Amount = Amount
        self.Purpose = Purpose
        self.FollowUp = FollowUp
        self.PreviousClaimID = PreviousClaimID
        self.Status = Status
        self.LastEditedClaimDate = LastEditedClaimDate

    def json(self):
        return {"ClaimID": self.ClaimID, "InsuranceID": self.InsuranceID, "FirstName": self.FirstName, "LastName": self.LastName, "ExpenseDate": self.ExpenseDate, "Amount": self.Amount, "Purpose": self.Purpose, "FollowUp": self.FollowUp, "PreviousClaimID": self.PreviousClaimID, "Status": self.Status, "LastEditedClaimDate": self.LastEditedClaimDate}

    # policies = db.relationship("PolicyModel", back_populates="claims")

    # def __repr__(self):
    #     return f"Policy(ClaimID = {self.ClaimID}, InsuranceID = {self.InsuranceID},\
    #             FirstName = {FirstName}, LastName = {LastName},\
    #             ExpenseDate = {ExpenseDate}, Amount = {Amount},\
    #             Purpose = {Purpose}, FollowUp = {FollowUp},\
    #             PreviousClaimID = {PreviousClaimID}, Status = {Status},\
    #             LastEditedClaimDate = {LastEditedClaimDate})"


@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    employeeID = data["EmployeeID"]
    user = UserModel.query.filter_by(UserModel.EmployeeID==employeeID).first()
    if user and user.Password == data["Password"]:
        return jsonify(
            {
                "code": 200,
                "data": user.json(),
                "message": "User logged in successfully."
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "User not found."
        }
    ), 404


@app.route("/getData/<int:employeeID>")
def getAllClaims(employeeID):
    claims = ClaimsModel.query.filter(ClaimsModel.EmployeeID==employeeID).all()
    if len(claims) > 0:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "claims": [claim.json() for claim in claims]
                },
                "message": "Claims found."
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no Staffs in the list.",

        }
    ), 404


@app.route("/editRecord/<int:employeeID>")
def editRecord(employeeID):
    claims = UserModel.query.filter(UserModel.EmployeeID==employeeID).all()
    if len(claims) > 0:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "claims": [claim.json() for claim in claims]
                },
                "message": "Claims found."
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no Staffs in the list.",

        }
    ), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)

