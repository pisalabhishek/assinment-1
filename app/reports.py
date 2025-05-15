from collections import defaultdict
from services import claims, get_policyholder_by_id

def monthly_claims():
    result = defaultdict(int)
    for claim in claims:
        month = claim.date[:7]
        result[month] += 1
    return dict(result)

def average_claim_by_policy():
    result = defaultdict(list)
    for claim in claims:
        policy = get_policyholder_by_id(claim.policyholder_id).policy_type
        result[policy].append(claim.amount)
    return {k: sum(v)/len(v) for k, v in result.items() if v}

def highest_claim():
    return max(claims, key=lambda x: x.amount, default=None)

def pending_claims():
    return [c for c in claims if c.status.lower() == 'pending']