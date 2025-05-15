policyholders = []
claims = []

def add_policyholder(data):
    policyholders.append(data)

def add_claim(data):
    claims.append(data)

def get_policyholder_by_id(pid):
    return next((p for p in policyholders if p.id == pid), None)

def get_claims_by_policyholder(pid):
    return [c for c in claims if c.policyholder_id == pid]

def calculate_claim_ratio(policyholder):
    user_claims = get_claims_by_policyholder(policyholder.id)
    total = sum(c.amount for c in user_claims)
    return total / policyholder.sum_insured if policyholder.sum_insured > 0 else 0

def is_high_risk(policyholder):
    user_claims = get_claims_by_policyholder(policyholder.id)
    freq = len([c for c in user_claims if c.date.startswith("2025")])
    return freq > 3 or calculate_claim_ratio(policyholder) > 0.8