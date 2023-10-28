import unittest
from app import *
from datetime import datetime


class TestCalc(unittest.TestCase):
    def test_handle_sms(self):
        handle_sms("tsla")

    def test_get_stock_price(self):
        get_stock_price("tsla")

    def test_message_structure(self):
        date = datetime.now()
        message_structure(date, "Tsla", 200.01, 300.03, 400.04, 500.05)


if __name__ == "__main__":
    unittest.main()
