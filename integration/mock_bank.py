import uuid

def send_payment(amount: float):
    return {
        "ref": str(uuid.uuid4()),
        "amount": amount,
        "status": "paid"
    }
