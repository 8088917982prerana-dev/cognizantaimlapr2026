from models.abc_banking_group import ABCBankingGroup
from models.savings_account import savings_account
def test_add_account():
    bank = ABCBankingGroup()
    sa = savings_account(1000, "2023-01-01", 0.05)
    bank.add_account(sa)
    assert len(bank.accounts) == 1