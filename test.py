import yfinance as yf
from datetime import datetime
import pandas as pd


company=['NVDA', 'AAPL', 'TSLA', 'GOOGL']

holders_data={}
for holders in company: 
    ticker=yf.Ticker(holders)
    holders_data[holders]=ticker.get_cashflow()

for holders, holders_df in holders_data.items():
    print(f'Institutional Holders for {holders}: \n')
    print(holders_df)
    print('='*100)