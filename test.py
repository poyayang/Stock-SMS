import yfinance as yf
from datetime import datetime

company=input('Please enter the stock code').upper()
tickers=yf.Ticker(company)
company_hist=tickers.history(period='1d')
info_needed=company_hist[['Open', 'High', 'Low', 'Close']]
reframe_hist=info_needed.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)

print(reframe_hist)