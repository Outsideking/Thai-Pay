import json

def get_report():
    try:
        with open("data/ledger.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    total = sum(x["amount"] for x in data)

    return {
        "total_transactions": len(data),
        "total_amount": total,
        "data": data
    }
