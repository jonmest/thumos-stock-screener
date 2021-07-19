# Parent class
from abc import ABC, abstractmethod

# Misc.
import os


class DataFetcher(ABC):
    """
    Base class defining the interface of all data fetchers.
    They all should have (1) a way to download tickers in the given universe
    and (2) download stock data to a given directory.
    """

    def __init__(self, universe: str, path: str, verbose: bool = False) -> None:
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
        verbose: bool
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
        self.verbose = verbose
        self.tickers = None
    
    @abstractmethod
    def downloadTickers(self) -> "DataFetcher":
        """
        Downloading all tickers in the given universe.
        """
        return self

    @abstractmethod
    def downloadStockData(self) -> None:
        """
        Downloading the data for the 
        """
        return self