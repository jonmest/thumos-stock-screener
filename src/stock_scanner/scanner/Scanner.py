# Parent class
from abc import ABC, abstractmethod
from typing import List

# Misc.
from src.stock_scanner.stock.Stock import Stock
from ..condition.Condition import Condition
from ..stock_io.StockIO import StockIO
# Condition validation
from ..validator.Validator import Validator


# Data IO


class Scanner(ABC):
    """
    Abstract scanner class all scanners should inherit from. The abstract methods need to be implemented.

    Methods:
        - __init__
        - load_data
        - get_candidates
    """

    def __init__(self, conditions: List[Condition],
                 stock_io: StockIO, validator: Validator) -> None:
        """
        Args:
            conditions (List[Condition]):
                List of conditions stocks returned from scan should fulfill.
            stock_io (StockIO, optional):
                An instance of StockIO
            validator (Validator, optional):
                A reference to a Validator, the default is BasicValidator.
        """
        self.conditions: List[Condition] = conditions
        self.stock_io: StockIO = stock_io
        self.validator: Validator = validator

    @abstractmethod
    def load_data(self, period: int = 365, verbose: bool = False) -> "Scanner":
        """
        Loads all stock data required for the scan.

        Args:
            period (int):
                How many bars back you want data for each stock
            verbose (bool, optional):
                Whether the download should be verbose, i.e. show progress or what
                stock is currently being downloaded.
        """
        return self

    @abstractmethod
    def get_candidates(self, verbose: bool = False) -> List[Stock]:
        """
        Return candidate stocks from the scan.

        Args:
            verbose (bool, optional):
                Whether the process should be verbose, i.e. show progress or what
                stock is currently being analyzed.
        """
        pass
