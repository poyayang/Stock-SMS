import unittest
from app import *
from datetime import datetime


class TestCalc(unittest.TestCase):
    def test_get_stock_price(self):
        stock_price = get_stock_price("tsla")
        print(stock_price)

    def test_message_structure(self):
        date = datetime.now()
        message = message_structure(date, "Tsla", 200.01, 300.03, 400.04, 500.05)
        print(message)


if __name__ == "__main__":
    unittest.main()
