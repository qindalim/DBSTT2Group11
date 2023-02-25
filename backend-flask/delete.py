@app.route("/deleteRecord/<int:employeeID>/<int:claimID>", methods=["DELETE"])
def deleteRecord(employeeID, claimID):
    # data = request.get_json()
    # employeeID = data["EmployeeID"]
    # claimID = data["ClaimID"]
    
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