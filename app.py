from fastapi import FastAPI
from core.payment import pay
from core.report import get_report

app = FastAPI(title="ThaiPay")

@app.post("/pay")
def payment(amount: float):
    return pay(amount)

@app.get("/report")
def report():
    return get_report()
