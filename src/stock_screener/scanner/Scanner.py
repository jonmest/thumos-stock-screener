# Parent class
from abc import ABC, abstractmethod

# Data IO
from ..data_reader.CSVReader import CSVReader
from ..data_reader.DataReader import DataReader
from ..data_fetcher.DataFetcher import DataFetcher
from ..data_fetcher.YahooDataFetcher import YahooDataFetcher

# Condition validation
from ..validator.Validator import Validator
from ..validator.BasicValidator import BasicValidator

# Misc.
from ..Stock import Stock
from typing import List
from ..condition.Condition import Condition
import warnings


class Scanner(ABC):
    def __init__(self, universe: str, conditions: List[Condition],
                data_fetcher: DataFetcher = YahooDataFetcher, data_reader: DataReader = CSVReader,
                validator: Validator = BasicValidator) -> None:
        if universe is None:
            raise ValueError("No universe was provided.")
        if conditions is None or len(conditions) < 1:
            warnings.warn("No conditions were given. This means all stocks in the given universe will be returned.")

        self.universe: str = universe
        self.conditions: List[Condition] = conditions
        self.data_fetcher = data_fetcher
        self.data_reader = data_reader
        self.validator = validator

    @abstractmethod
    def loadData(self, path: str, verbose: bool = False) -> None:
        pass

    @abstractmethod
    def getCandidates(self, verbose: bool = False) -> List[Stock]:
        pass