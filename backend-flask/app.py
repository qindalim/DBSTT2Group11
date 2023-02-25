from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost:3306/insurancedata"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
CORS(app)

db = SQLAlchemy(app)


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


class ClaimsModel(db.Model):
    __tablename__ = "InsuranceClaims"

    ClaimID = db.Column(db.Integer, primary_key=True, nullable=False)
    InsuranceID = db.Column(db.Integer,  
                            db.ForeignKey("InsurancePolicies.InsuranceID", ondelete="CASCADE"), 
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


@app.route("/getData/<int:employeeID>", methods=["GET"])
def getAllClaims(employeeID):
    policies = PolicyModel.query.filter(PolicyModel.EmployeeID==employeeID).all()
    policies = [policy.json() for policy in policies]
    claims = {}
    for policy in policies:
        claims = ClaimsModel.query.filter(ClaimsModel.InsuranceID==policy["InsuranceID"]).all()
        
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


@app.route("/editRecord", methods=["PUT"])
def editRecord():
    data = request.get_json()
    claimID = data["ClaimID"]

    claim = ClaimsModel.query.filter(ClaimsModel.ClaimID==claimID).first()
    # policies = PolicyModel.query.filter(and_(PolicyModel.EmployeeID==employeeID, PolicyModel.InsuranceID==insuranceID)).all()
    # claims = ClaimsModel.query.filter(and_(ClaimsModel.InsuranceID==policies.InsuranaceID, ClaimsModel.ClaimID==claimID)).all()

    if claim:
        claim.FirstName = data["FirstName"]
        claim.LastName = data["LastName"]
        claim.ExpenseDate = data["ExpenseDate"]
        claim.Amount = data["Amount"]
        claim.Purpose = data["Purpose"]
        claim.FollowUp = data["FollowUp"]
        claim.PreviousClaimID = data["PreviousClaimID"]
        claim.Status = data["Status"]
        claim.LastEditedClaimDate = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+08:00')

        try:
            db.session.commit()
            return jsonify(
                    {
                        "code": 200,
                        "message": "Patient chat data updated.",
                        "data": claim.json()
                    }
                ), 200
        except:
            return jsonify(
                {
                    "code": 500,
                    "message": "Server error try again later"
                }
            ), 500
        
@app.route("/addRecord", methods=["POST"])
def addRecord():
    data = request.get_json()
    claim = ClaimsModel(**data)
    try:
        db.session.add(claim)
        db.session.commit()

    except:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred adding of claim.",
                "data": {
                    "ClaimID": data["ClaimID"]
                }
            }
        ), 500
    return jsonify(
        {
            "code": 201,
            "message": "Claim created.",
            "data": claim.json()
        }
    ), 201

@app.route("/deleteRecord", methods=["DELETE"])
def deleteRecord():
    data = request.get_json()
    employeeID = data["EmployeeID"]
    claimID = data["ClaimID"]
    
    policy_result = PolicyModel.query.filter_by(EmployeeID=employeeID).all()

    insurance_id_lst = []
    for i in policy_result:
        insurance_id_lst.append(i.InsuranceID)
    
    claim_result = []
    claim_id_lst = []
    for insurance_id in insurance_id_lst:
        temp = ClaimsModel.query.filter_by(InsuranceID=insurance_id).all()
        for i in temp:
            claim_id_lst.append(i.ClaimID)
            claim_result.append(i)

    if claimID in claim_id_lst:
        claim = ClaimsModel.query.get(claimID)
        db.session.delete(claim)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "message": f"Claim {claimID} deleted."
            }
        ), 200

    return jsonify(
        {
            "code": 404,
            "message": "Claim does not belong to employee.",

        }
    ), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

