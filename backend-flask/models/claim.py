from db import db

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
    Purpose = db.Column(db.String(255), nullable=False)
    FollowUp = db.Column(db.Boolean, nullable=False)
    Purpose = db.Column(db.String(255), nullable=False)
    PreviousClaimID = db.Column(db.Integer, nullable=False)
    Status = db.Column(db.String(20), nullable=False)
    LastEditedClaimDate = db.Column(db.String(255), nullable=False)

    
    policies = db.relationship("PolicyModel", back_populates="claims")

