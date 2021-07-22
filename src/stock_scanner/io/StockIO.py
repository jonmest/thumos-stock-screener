"""
This module contains the abstract class defining the interface ALL 
DataReaders need to implement.
"""

# Parent class
from abc import ABC, abstractmethod
from typing import List

from stock_scanner.data_fetcher.DataFetcher import DataFetcher

# Misc.
from ..Stock import Stock
import os
from datetime import datetime

class StockIO(ABC):
    """
    IO abstract class
    """

    @abstractmethod
    def __init__(self, universe: str, path: str) -> None:
        """
        Args:
            universe (str): The name of the universe (one implementation could for example allow "nasdaq" or "sp500")
            path (str): The path to the directory the stock data should be downloaded.
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

    def getTickers(self) -> List[str]:
        """
        A convenient getter method for the ticker list.
        """
        if os.environ.get('MAX_TICKERS'):
            return self.tickers[:int(os.environ.get('MAX_TICKERS'))]
        else:
            return self.tickers

    @abstractmethod
    def read(self, ticker: str, path: str) -> Stock:
        """
        Read data from file and return a Stock instance. A stock ticker (e.g. "AAPL") and
        directory path should be given, and the file name resolution should be the concern
        of this method.

        Args:
            ticker (str): Ticker of the stock (e.g. "AAPL").
            path (str): Path to the the ticker's file.
        """
        pass