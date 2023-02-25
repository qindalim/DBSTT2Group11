from db import db


class PolicyModel(db.Model):
    __tablename__ = "InsurancePolicies"

    InsuranceID = db.Column(db.Integer, primary_key=True)
    EmployeeID = db.Column(db.Integer, 
                           db.ForeignKey("User.employeeId", ondelete="CASCADE"), 
                           nullable=False)
    InsuranceType = db.Column(db.String(100), nullable=False)
    PolicyStartDate = db.Column(db.String(255), nullable=False)
    PolicyTerm = db.Column(db.String(100), nullable=False)
    PolicyEndDate = db.Column(db.String(255), nullable=False)
    ClaimLimit = db.Column(db.Float(precision=2), nullable=False)
    RemainingClaimLimit = db.Column(db.Float(precision=2), nullable=False)

    users = db.relationship("UserModel", back_populates="policies")
    claims = db.relationship(
        "ClaimsModel",
        back_populates="InsurancePolicies",
        cascade="all, delete",
        passive_deletes=True,
    )    

    def __repr__(self):
        return f"Policy(InsuranceID = {InsuranceID}, EmployeeID = {EmployeeID},\
                InsuranceType = {InsuranceType}, PolicyStartDate = {PolicyStartDate},\
                PolicyTerm = {PolicyTerm}, PolicyEndDate = {PolicyEndDate},\
                ClaimLimit = {ClaimLimit}, RemainingClaimLimit = {RemainingClaimLimit})"

    
