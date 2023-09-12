import unittest
import calc
import yfinance as yf
from datetime import datetime
import pandas as pd
import math


class TestCalc(unittest.TestCase): 
    def test_current_price(self):
        company=input('What company would you like to look up?').upper()
        tickers=yf.Ticker(company)
        company_hist=pd.DataFrame(tickers.history(period='1d'))
        info_needed=company_hist[['Open', 'High', 'Low', 'Close']]
        reframe_hist=info_needed.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)
        print(reframe_hist)

    def test_data_history(self): 
        company=input('What company you would like to look up?')
        tickers=yf.Ticker(company)
        end_date=datetime.now().strftime('%Y-%m-%d')
        company_hist=tickers.history(period='max', start='2023-08-01', end=end_date, interval='1h')
        reframe_hist=company_hist.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)
        print(reframe_hist)
    
    def test_company_institutional_holders(self): 
        holders_data={}
        company=input("Enter company stock code: ").split() # split() works for both singular and multiple codes
        for holders in company: 
            ticker=yf.Ticker(holders)
            holders_data[holders]=ticker.get_institutional_holders()

        for holders, holders_df in holders_data.items():
            print(f'Institutional Holders for {holders}: \n')
            print(holders_df)
            print('='*100)
    
    def test_cash_flow_history(self):
        holders_cashflow={}
        company=input("Enter company stock code: ").split() # split() works for both singular and multiple codes
        for cashflow in company: 
            ticker=yf.Ticker(cashflow)
            holders_cashflow[cashflow]=ticker.get_cash_flow()

        for cashflow, cashflow_df in holders_cashflow.items(): 
            print(f'Cashflow history for {cashflow}:\n')
            print(cashflow_df)
            print('///'*50)
    
    def test_options_chain(self): 
        company=input('Enter the company stock code:')
        ticker=yf.Ticker(company)
        options=ticker.option_chain()
        option_puts=options.puts
        option_calls=options.calls
        print("Put Options:")
        print(option_puts)
        print("=" * 50)
        print("Call Options:")
        print(option_calls)


if __name__=='__main__':
    unittest.main()