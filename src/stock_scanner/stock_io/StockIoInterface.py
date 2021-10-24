"""
This module contains the abstract class defining the interface ALL 
DataReaders need to implement.
"""

# Parent class
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

# Misc.
from src.stock_scanner.stock.Stock import Stock


class StockIoInterface(ABC):
    """
    IO abstract class
    """

    @abstractmethod
    def __init__(self, universe: str, path: str, max_tickers: int) -> None:
        """
        Args:
            universe (str): The name of the universe (one implementation could for example allow "nasdaq" or "sp500")
            path (str): The path to the directory the stock data should be downloaded.
            max_tickers (int)
        """
        pass

    @abstractmethod
    def download_stock_data(self, start_date: datetime, end_date: datetime, verbose: bool) -> "StockIoInterface":
        """
        Downloading the data for stocks in the given the given universe.

        Args: start_date (datetime): From when should the data be downloaded (e.g. "let's download data from
        2020-06-18") end_date (datetime): Until when should the data be downloaded (e.g. "let's download data from
        2020-06-18 to 2021-06-18") verbose (bool, optional): Whether the download should be verbose, for example by
        displaying progress or which ticker is currently being downloaded. Handy for debugging purposes.
        """
        pass

    def get_tickers(self) -> List[str]:
        """
        A convenient getter method for the ticker list.
        """
        raise NotImplementedError()

    @abstractmethod
    def read(self, ticker: str, start_date: datetime, end_date: datetime) -> Stock:
        """
        Read data from file and return a Stock instance. A stock ticker (e.g. "AAPL") and
        directory path should be given, and the file name resolution should be the concern
        of this method.

        Args:
            start_date (datetime)
            end_date (datetime)
            ticker (str): Ticker of the stock (e.g. "AAPL").
        """
        pass
