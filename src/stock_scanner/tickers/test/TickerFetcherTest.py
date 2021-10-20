from ..TickerFetcher import TickerFetcher
import unittest


class TickerFetcherTest(unittest.TestCase):
    def test_get_dow(self):
        ticker_fetcher = TickerFetcher()
        for ticker in ticker_fetcher.getDow():
            self.assertIsInstance(ticker, str)

    def test_get_sp500(self):
        ticker_fetcher = TickerFetcher()
        for ticker in ticker_fetcher.getSP500():
            self.assertIsInstance(ticker, str)

    def test_get_nasdaq(self):
        ticker_fetcher = TickerFetcher()
        for ticker in ticker_fetcher.getNasdaq():
            self.assertIsInstance(ticker, str)

    def test_get_stockholm(self):
        ticker_fetcher = TickerFetcher()
        for ticker in ticker_fetcher.getStockholm():
            self.assertIsInstance(ticker, str)


if __name__ == '__main__':
    unittest.main()
