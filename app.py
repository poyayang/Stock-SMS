import yfinance as yf
import logging
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from datetime import date

app = Flask(__name__)


@app.route("/sms", methods=["POST"])
def sms() -> str:
    number = request.form["From"]
    stock_symbol = request.form["Body"]
    logging.info(f"received request from {number}: {stock_symbol}")
    message = handle_sms(stock_symbol)
    return message


def handle_sms(stock_symbol: str) -> str:
    stock_prices = get_stock_price(stock_symbol)
    message = message_structure(
        date.today(),
        stock_symbol,
        stock_prices["Open"],
        stock_prices["Close"],
        stock_prices["High"],
        stock_prices["Low"],
    )
    resp = MessagingResponse()
    resp.message(message)
    return str(resp)


def get_stock_price(company: str) -> dict:
    tickers = yf.Ticker(company)
    company_hist = tickers.history(period="1d")
    prices = company_hist[["Open", "High", "Low", "Close"]]
    price = {
        "Date": date.today().strftime("%y-%m-%d"),
        "Open": prices["Open"].values[0],
        "Close": prices["Close"].values[0],
        "High": prices["High"].values[0],
        "Low": prices["Low"].values[0],
    }
    return price


def message_structure(
    date: date, ticker: str, open: float, close: float, high: float, low: float
) -> str:
    strdate = date.strftime("%y-%m-%d")
    message = f"Date:{strdate}\nCompany:{ticker}\nOpen:{open:.2f}\nClose:{close:.2f}\nHigh:{high:.2f}\nLow:{low:.2f}"
    return message


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    app.app_context().push()
