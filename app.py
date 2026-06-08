from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import joblib
import csv
import pandas as pd

app = FastAPI()

# Load model
model = joblib.load("model.pkl")

# Templates
templates = Jinja2Templates(directory="templates")

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    try:
        logs = pd.read_csv("logs.csv")
        history = logs.tail(5).values.tolist()[::-1]
        total_predictions = len(logs)
    except:
        history = []
        total_predictions = 0

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "history": history,
            "total_predictions": total_predictions
        }
    )


@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, text: str = Form(...)):

    prediction = model.predict([text])[0]

    # Save prediction to logs.csv
    with open("logs.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([text, prediction])

    logs = pd.read_csv("logs.csv")
    history = logs.tail(5).values.tolist()[::-1]
    total_predictions = len(logs)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "prediction": prediction,
            "text": text,
            "history": history,
            "total_predictions": total_predictions
        }
    )