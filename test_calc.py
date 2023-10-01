import unittest
#import calc
import yfinance as yf
from datetime import datetime
import pandas as pd
import math

from secondary import *

class TestCalc(unittest.TestCase): 
    def test_current_price(self):
        current_price

    def test_data_history(self):
        data_history

    def test_company_institutional_holders(self): 
        company_institutional_holders
    
    def test_cash_flow_history(self): 
        cash_flow_history
    
    def test_option_chain(self):
        options_chain


if __name__=='__main__':
    unittest.main()