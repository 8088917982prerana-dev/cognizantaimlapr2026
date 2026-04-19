from models.direct_debit import direct_debit
def test_transaction():
    dd = direct_debit(100, "2023-01-01", "John", "Electric Company", "2023-01-15")
    assert dd.amount == 100
    assert dd.payment_date == "2023-01-15"