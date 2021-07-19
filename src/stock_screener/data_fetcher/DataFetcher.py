# Parent class
from abc import ABC, abstractmethod
from datetime import datetime

# Misc.
import os
from typing import List


class DataFetcher(ABC):
    """
    Base class defining the interface of all data fetchers.
    They all should have (1) a way to download tickers in the given universe
    and (2) download stock data to a given directory.
    """

    def __init__(self, universe: str, path: str) -> None:
        """
        Parameters
        ----------
        universe: str
            The name of the universe (one implementation could for example allow "nasdaq" or "sp500")
        path: str
            The path to where the stock data should be downloaded.
        verbose: bool, optional
            Whether the fetching should be verbose (display progress etc.) or not. Default is False.

        Attributes
        ----------
        universe: str
        path: str
        tickers: List[str]
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
        Downloading all tickers in the given universe.
        """
        return self

    
    @abstractmethod
    def getTickers(self) -> List[str]:
        """
        Return a list of tickers from the universe.
        """
        pass

    @abstractmethod
    def downloadStockData(self, start_date: datetime, end_date: datetime, verbose: bool = False) -> None:
        """
        Downloading the data for the given universe.
        """
        return self

    @abstractmethod
    def getTickerPath(self, ticker: str) -> str:
        """
        Return the path to the file for a stock
        """
        pass