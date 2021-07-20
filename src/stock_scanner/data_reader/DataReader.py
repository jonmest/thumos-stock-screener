"""
This module contains the abstract class defining the interface ALL 
DataReaders need to implement.
"""

# Parent class
from abc import ABC, abstractmethod

# Misc.
from ..Stock import Stock


class DataReader(ABC):
    """
    DataReader abstract class
    """

    @abstractmethod
    def __init__(self) -> None:
        """
        No specified interface here. However, DataReader implementations should be
        be concerned with information such as formatting of the data, value mapping 
        and similar things in the constructor. See CSVReader as an example.
        """
        pass

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