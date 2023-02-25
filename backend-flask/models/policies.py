from db import db


class PoliciesModel(db.Model):
    __tablename__ = "InsurancePolicies"

    insuranceId = db.Column(db.Integer, primary_key=True)
    employeeId = db.Column(db.Integer, db.ForeignKey("User.employeeId"), nullable=False, ondelete="CASCADE")
    insuranceType = db.Column(db.String(100), nullable=False)
    policyStartDate = db.Column(db.String(255), nullable=False)
    policyTerm = db.Column(db.String(100), nullable=False)
    policyEndDate = db.Column(db.String(255), nullable=False)
    claimLimit = db.Column(db.Float(precision=2), nullable=False)
    remainingClaimLimit = db.Column(db.Float(precision=2), nullable=False)

    employeeIdConstraint = db.relationship("employeeId", backref=db.backref("User", cascade="update, delete", back_populates="employeeId"))
    
