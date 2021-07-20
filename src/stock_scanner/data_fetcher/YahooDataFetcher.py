# Parent class
from datetime import datetime
from ..data_fetcher.DataFetcher import DataFetcher

# Misc.
import os
import pandas as pd
import os

# We use yahooquery instead of the more popular Yfinance, and highly recommed you do too
from yahooquery import Ticker
from typing import List
from yahoo_fin import stock_info as si


class YahooDataFetcher(DataFetcher):
    def __init__(self, universe: str, path: str) -> None:
        """
        A DataFetcher downloading OHLC data from Yahoo Finance. There are rate limits, but it should
        realistically not be a problem. It makes use of yahooquery, which also has the capability to
        download more qualitative data - if you're interested in that for a custom DataFetcher.

        It also downloads the stock data in CSV format. If you develop a custom DataFetcher you may use
        a different format, but remember to use a compatible DataReader in that case.

        Args:
            universe (str, ["sp500", "nasdaq", "dow", "ftse100", "ftse250", "nifty50", "niftybank"]):
                The name of the universe.
            path (str):
                The path to where the stock data should be downloaded.
            verbose (bool, optional):
                Whether the fetching should be verbose (display progress etc.) or not. Default is False.

        Attributes:
            universe (str): universe
            path (str): path
            tickers (List[str]): tickers
        """
        valid_universes: List[str] = ["nasdaq", "dow", "ftse100", "ftse250", "nifty50", "niftybank", "sp500"]
        if universe not in valid_universes:
            raise ValueError("Invalid universe given.")
        super().__init__(universe, path)

    def downloadTickers(self) -> "YahooDataFetcher":
        """
        Downloading/reading a list of all tickers in the given universe and sets them as self.tickers
        Note, that it returns `self` to allow for method chaining.
        """
        if self.universe == "sp500":
            self.tickers = si.tickers_sp500()
        elif self.universe == "nasdaq":
            self.tickers = si.tickers_nasdaq()
        elif self.universe == "dow":
            self.tickers = si.tickers_dow()
        elif self.universe == "ftse100":
            self.tickers = si.tickers_ftse100()
        elif self.universe == "ftse250":
            self.tickers = si.tickers_ftse250()
        elif self.universe == "nifty50":
            self.tickers = si.tickers_nifty50()
        elif self.universe == "niftybank":
            self.tickers = si.tickers_niftybank()

        # Yahoo Finance uses dashes instead of dots
        self.tickers: List[str] = [item.replace(".", "-") for item in self.tickers]
        return self
    
    def getTickers(self) -> List[str]:
        """
        A convenient getter method for the ticker list.
        """
        if os.environ.get('MAX_TICKERS'):
            return self.tickers[:int(os.environ.get('MAX_TICKERS'))]
        else:
            return self.tickers


    def downloadStockData(self, start_date: datetime, end_date: datetime, verbose: bool = False) -> None:
        """
        Downloading the data for stocks in the given the given universe.

        Args:
            start_date (datetime): From when should the data be downloaded (e.g. "let's download data from 2020-06-18")
            end_date (datetime): Until when should the data be downloaded (e.g. "let's download data from 2020-06-18 to 2021-06-18")
            verbose (bool, optional): Whether the download should be verbose, for example by displaying progress or which ticker is
                currently being downloaded. Handy for debugging purposes.
        """
        if os.environ.get('MAX_TICKERS'):
            tickers = self.tickers[:int(os.environ.get('MAX_TICKERS'))]
        else:
            tickers = self.tickers

        for ticker in tickers:
            if verbose:
                print("Downloading data for ticker", ticker)
            df: pd.DataFrame = Ticker(ticker).history(start=start_date, end=end_date)
            try:
                df.to_csv(os.path.join(self.path, f"{ticker}.csv"))
            except Exception:
                if verbose:
                    print("Failed to save data for ticker", ticker)

        return self

    
    def getTickerPath(self, ticker: str) -> str:
        """
        Return the path to the file for a stock.

        Args:
            ticker (str): Ticker for a stock (e.g. "AAPL")
        """
        return os.path.join(self.path, f"{ticker}.csv")