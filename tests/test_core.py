from models import Policyholder
from services import is_high_risk, add_claim

def test_high_risk():
    ph = Policyholder(1, "John", 35, "Life", 100000)
    for i in range(4):
        add_claim(type("Claim", (), {
            "claim_id": i, "policyholder_id": 1,
            "amount": 30000, "reason": "Test",
            "status": "Approved", "date": "2025-05-10"
        })())
    assert is_high_risk(ph)