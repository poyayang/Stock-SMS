import yfinance as yf
import logging
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from datetime import date

app = Flask(__name__)


@app.route("/sms", methods=["POST"])
def sms() -> str:
    number = request.form.get["From"]
    stock_symbol = request.form.get["Body"]
    logging.info(f"received request from {number}: {stock_symbol}")
    message = handle_sms(stock_symbol)
    return message


@app.route("/", methods=["GET"])
def render_get() -> str:
    get_slash='OK'
    return get_slash


def handle_sms(stock_symbol: str) -> str:
    date, open, close, high, low = get_stock_price(stock_symbol)
    message = message_structure(
        date,
        stock_symbol,
        open,
        close,
        high,
        low,
    )
    resp = MessagingResponse()
    resp.message(message)
    return str(resp)


def get_stock_price(company: str):
    tickers = yf.Ticker(company)
    company_hist = tickers.history(period="1d")
    prices = company_hist[["Open", "High", "Low", "Close"]]

    stock_date = date.today()
    open = prices["Open"].values[0]
    close = prices["Close"].values[0]
    high = prices["High"].values[0]
    low = prices["Low"].values[0]

    return stock_date, open, close, high, low


def message_structure(
    stock_date: date, ticker: str, open: float, close: float, high: float, low: float
) -> str:
    strdate = stock_date.strftime("%y-%m-%d")
    message = f"Date:{strdate}\nCompany:{ticker}\nOpen:{open:.2f}\nClose:{close:.2f}\nHigh:{high:.2f}\nLow:{low:.2f}"
    return message


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    app.app_context().push()
