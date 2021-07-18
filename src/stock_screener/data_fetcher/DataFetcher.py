# Parent class
from abc import ABC, abstractmethod

# Misc.
import os


class DataFetcher(ABC):
    def __init__(self, universe: str, path: str, verbose: bool = False) -> None:
        if universe is None:
            raise ValueError('The name of a universe needs to be supplied. For example, \"^IXIC\" for NASDAQ stocks.')
        if universe is None:
            raise ValueError('A path for where the stock data should be downloaded is required.')    
        self.universe = universe

        if not os.path.exists(path):
            os.makedirs(path)
        self.path = path
        self.verbose = verbose
    
    @abstractmethod
    def downloadTickers(self) -> None:
        pass

    @abstractmethod
    def downloadStockData(self, path: str) -> None:
        pass