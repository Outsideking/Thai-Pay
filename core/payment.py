from core.accounting import record_ledger
from integration.mock_bank import send_payment

def pay(amount: float):
    result = send_payment(amount)
    record_ledger(amount)
    return {
        "status": "success",
        "amount": amount,
        "bank_ref": result["ref"]
    }
