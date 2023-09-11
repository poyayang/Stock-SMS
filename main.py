import yfinance as yf
from datetime import datetime
import pandas as pd
       
from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse

app=Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms(): 
    number=request.form['From']
    message_body=request.form['Body']
    
    tickers=yf.Ticker(message_body)
    company_hist=tickers.history(period='1d')
    info_needed=company_hist[['Open', 'High', 'Low', 'Close']]
    data_list=[]
    for index, row in info_needed.iterrows():
        data_dict={'Date': index.strftime('%Y-%m-%d'), 
                   'Ticker': message_body.upper(), 
                   'Open': row['Open'],
                   'High': row['High'],
                   'Low': row['Low'],
                   'Close': row['Close']}
        data_list.append(data_dict)
    response_content='Hello {}, here is the stock info:\n'.format(number)
    for data in data_list:
        response_content += 'Date: {}\nTicker: {}\nOpen: {}\nHigh: {}\nLow: {}\nClose: {}\n\n'.format(
        data['Date'], data['Ticker'], data['Open'], data['High'], data['Low'], data['Close'])

    response=MessagingResponse()
    response.message(response_content)
    return str(response)

#@app.route('/hello', methods=['GET'])
#def hell_world():
#    a='hello world'
#    return a

if __name__=='__main__':
    app.run(port=5002)



