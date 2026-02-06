from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from core.payment import pay
from core.report import get_report

app = FastAPI(title="ThaiPay")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

@app.post("/pay")
def payment(amount: float):
    return pay(amount)

@app.get("/report")
def report():
    return get_report()
