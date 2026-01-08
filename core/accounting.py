import json
from datetime import datetime

LEDGER_FILE = "data/ledger.json"

def record_ledger(amount: float):
    entry = {
        "time": datetime.utcnow().isoformat(),
        "amount": amount,
        "type": "credit"
    }

    try:
        with open(LEDGER_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open(LEDGER_FILE, "w") as f:
        json.dump(data, f, indent=2)
