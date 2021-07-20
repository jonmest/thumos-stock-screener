# Parent class
from abc import ABC, abstractmethod

# Misc.
from ..Stock import Stock


class DataReader(ABC):
    """
    Abstract class for reading in stock data from a file
    and returning a Stock instance.
    """
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def read(self, ticker: str, path: str) -> Stock:
        """
        Read data and return stock.

        Parameters
        ----------
        ticker: str
            Ticker of the stock
        path: str
            Path to stock's data file
        """
        pass