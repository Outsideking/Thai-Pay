from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from core.payment import pay
from core.report import get_report

app = FastAPI(title="ThaiPay")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """Homepage with Speed Insights enabled"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/pay")
def payment(amount: float):
    return pay(amount)

@app.get("/report")
def report():
    """JSON API endpoint for report"""
    return get_report()

@app.get("/report-view", response_class=HTMLResponse)
def report_view(request: Request):
    """HTML view of report with Speed Insights enabled"""
    report_data = get_report()
    return templates.TemplateResponse("report.html", {
        "request": request,
        "report": report_data
    })
