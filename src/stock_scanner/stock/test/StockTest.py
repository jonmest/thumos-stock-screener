import unittest

import pandas as pd

from ..stock import Stock


class StockTest(unittest.TestCase):

    def setUp(self) -> None:
        self.__ticker = "TEST"
        self.__stock_data = {
            "open": [1, 2, 3, 4, 5],
            "close": [2, 3, 4, 5, 6],
            "high": [3, 4, 5, 6, 7],
            "low": [0, 1, 2, 3, 4],
            "volume": [100, 200, 300, 400, 500],
            "date": ["2020-01-01", "2020-01-02", "2020-01-03", "2020-01-04", "2020-01-05"]
        }
        self.__df = pd.DataFrame.from_dict(self.__stock_data)
        self.__stock = Stock(self.__ticker, self.__df, "close",
                             "volume", "open", "high",
                             "low", "date")

    def test_can_get_close(self):
        expected = self.__stock_data["close"]
        actual = self.__stock.get_close()

        self.assertEqual(len(expected), len(actual))
        for e, a in zip(expected, actual):
            self.assertEqual(e, a)

    def test_can_get_open(self):
        expected = self.__stock_data["open"]
        actual = self.__stock.get_open()

        self.assertEqual(len(expected), len(actual))
        for e, a in zip(expected, actual):
            self.assertEqual(e, a)

    def test_can_get_low(self):
        expected = self.__stock_data["low"]
        actual = self.__stock.get_low()

        self.assertEqual(len(expected), len(actual))
        for e, a in zip(expected, actual):
            self.assertEqual(e, a)

    def test_can_get_high(self):
        expected = self.__stock_data["high"]
        actual = self.__stock.get_high()

        self.assertEqual(len(expected), len(actual))
        for e, a in zip(expected, actual):
            self.assertEqual(e, a)

    def test_can_get_volume(self):
        expected = self.__stock_data["volume"]
        actual = self.__stock.get_volume()

        self.assertEqual(len(expected), len(actual))
        for e, a in zip(expected, actual):
            self.assertEqual(e, a)

    def test_can_get_date(self):
        expected = self.__stock_data["date"]
        actual = self.__stock.get_date()

        self.assertEqual(len(expected), len(actual))
        for e, a in zip(expected, actual):
            self.assertEqual(e, a)

    def test_has_column(self):
        self.assertTrue(self.__stock.has_column("close"))
        self.assertFalse(self.__stock.has_column("Mark Minervini"))


if __name__ == '__main__':
    unittest.main()
