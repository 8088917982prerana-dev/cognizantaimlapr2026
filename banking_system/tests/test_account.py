from models.current_account import current_account
from models.savings_account import savings_account
def test_savings_account():
    sa = savings_account(1000, "2023-01-01", 0.05)
    assert sa.running_total == 1000
    assert sa.interest_rate == 0.05

def test_current_account():
    ca = current_account(2000, "2023-01-01", 500)
    assert ca.running_total == 2000
    assert ca.overdraft_limit == 500