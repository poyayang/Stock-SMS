import yfinance as yf
from datetime import datetime
import pandas as pd

def current_price():
    company=input('What company would you like to look up?').upper()
    tickers=yf.Ticker(company)
    company_hist=pd.DataFrame(tickers.history(period='1d'))
    info_needed=company_hist[['Open', 'High', 'Low', 'Close']]
    reframe_hist=info_needed.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)
    print(reframe_hist)


def data_history(): 
    company=input('What companies you would like to look up?')
    tickers=yf.Tickers(company)
    end_date=datetime.now().strftime('%Y-%m-%d')
    company_hist=tickers.history(period='max', start='2023-08-01', end=end_date, interval='1h')
    reframe_hist=company_hist.stack(level=1).rename_axis(['Date', 'Ticker']).reset_index(level=1)

    print(reframe_hist)



def company_institutional_holders(): 
    holders_data={}
    company=input("Enter company stock code: ").split() # split() works for both singular and multiple codes
    for holders in company: 
        ticker=yf.Ticker(holders)
        holders_data[holders]=ticker.get_institutional_holders()

    for holders, holders_df in holders_data.items():
        print(f'Institutional Holders for {holders}: \n')
        print(holders_df)
        print('='*100)


def cash_flow_history():
    holders_cashflow={}
    company=input("Enter company stock code: ").split() # split() works for both singular and multiple codes
    for cashflow in company: 
        ticker=yf.Ticker(cashflow)
        holders_cashflow[cashflow]=ticker.get_cash_flow()

    for cashflow, cashflow_df in holders_cashflow.items(): 
        print(f'Cashflow history for {cashflow}:\n')
        print(cashflow_df)
        print('///'*50)


def options_chain(): 
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


def enter_request(prompt, retries=4, reminder='Invalid input, please try again.'):
    while True: 
        ans=input(prompt).lower()
        if ans in ('1', 'current price', '1. current price'):
            return current_price()
        if ans in ('2', 'data history', '1. data history'): 
            return data_history()
        if ans in ('3', 'company institutional holders', '2. company institutional holders'): 
            return company_institutional_holders()
        if ans in ('4', 'cash flow history', '3. cash flow history'):
            return cash_flow_history()
        if ans in ('5', 'options chain', '4. options chain'): 
            return options_chain()
        else:     
            retries=retries-1
            if retries==0:
                raise ValueError('Invalid request')
            print(reminder)

def sms_response(self):
    prompt='1. Current Price, 2. Data History, 3. Company Institutional Holders, 4. Cash Flow History, 5. Options Chain, what would you to know? '
    content=enter_request(prompt)
    return str(content)


# enter_request('1. Current Price, 2. Data History, 3. Company Institutional Holders, 4. Cash Flow History, 5. Options Chain, what would you like to know? ', retries=4, reminder='Please try again.')
