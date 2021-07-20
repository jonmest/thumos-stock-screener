# Parent class
from abc import ABC, abstractmethod
from datetime import datetime

# Misc.
import os
from typing import List


class DataFetcher(ABC):
    """
    Base class defining the interface of all data fetchers.
    """

    def __init__(self, universe: str, path: str) -> None:
        """
        Args:
            universe (str): The name of the universe (one implementation could for example allow "nasdaq" or "sp500")
            path (str): The path to where the stock data should be downloaded.
        """
        if universe is None:
            raise ValueError('The name of a universe needs to be supplied. For example, \"^IXIC\" for NASDAQ stocks.')
        if universe is None:
            raise ValueError('A path for where the stock data should be downloaded is required.')    
        self.universe = universe

        if not os.path.exists(path):
            os.makedirs(path)
        self.path = path
        self.tickers = None
    
    @abstractmethod
    def downloadTickers(self) -> "DataFetcher":
        """
        Downloading/reading a list of all tickers in the given universe and sets them as self.tickers
        Note, that it should also return `self` to allow for method chaining.
        """
        self.tickers = []
        return self

    
    @abstractmethod
    def getTickers(self) -> List[str]:
        """
        A convenient getter method for the ticker list.
        """
        return self.tickers

    @abstractmethod
    def downloadStockData(self, start_date: datetime, end_date: datetime, verbose: bool = False) -> "DataFetcher":
        """
        Downloading the data for stocks in the given the given universe.

        Args:
            start_date (datetime): From when should the data be downloaded (e.g. "let's download data from 2020-06-18")
            end_date (datetime): Until when should the data be downloaded (e.g. "let's download data from 2020-06-18 to 2021-06-18")
            verbose (bool, optional): Whether the download should be verbose, for example by displaying progress or which ticker is
                currently being downloaded. Handy for debugging purposes.
        """
        return self

    @abstractmethod
    def getTickerPath(self, ticker: str) -> str:
        """
        Return the path to the file for a stock.

        Args:
            ticker (str): Ticker for a stock (e.g. "AAPL")
        """
        pass