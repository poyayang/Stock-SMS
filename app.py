from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import yfinance as yf
import pandas as pd
from datetime import datetime

app = Flask(__name__)


@app.route("/sms", methods=["POST"])
def sms() -> str:
    number = request.form["From"]
    stock_symbol = request.form["Body"]
    stock_prices = get_stock_price(stock_symbol)
    message = message_structure(lambda: stock_prices)
    resp = MessagingResponse()
    resp.message(message)
    return str(resp)


def get_stock_price(company: str) -> dict:
    tickers = yf.Ticker(company)
    company_hist = tickers.history(period="1d")
    prices = company_hist[["Open", "High", "Low", "Close"]]
    price = {
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Open": prices["Open"].values[0],
        "Close": prices["Close"].values[0],
        "High": prices["High"].values[0],
        "Low": prices["Low"].values[0],
    }

    return price


def message_structure(
    date: datetime, ticker: str, open: float, close: float, high: float, low: float
) -> str:
    strdate = str(date.strftime("%y-%m-%d"))
    message = f"Date:{strdate}\nCompany:{ticker}\nOpen:{open}\nClose:{close}\nHigh:{high}\nLow:{low}"
    return message


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    app.app_context().push()
