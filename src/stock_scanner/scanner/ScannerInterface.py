# Parent class
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

# Misc.
from src.stock_scanner.stock.Stock import Stock
from src.stock_scanner.condition.ConditionInterface import ConditionInterface
from src.stock_scanner.stock_io.StockIoInterface import StockIoInterface
# ConditionInterface validation
from src.stock_scanner.validator.ValidatorInterface import ValidatorInterface


# Data IO


class ScannerInterface(ABC):
    """
    Abstract scanner class all scanners should inherit from. The abstract methods need to be implemented.

    Methods:
        - __init__
        - load_data
        - get_candidates
    """

    def __init__(self, conditions: List[ConditionInterface],
                 stock_io: StockIoInterface, start_date: datetime, end_date: datetime,
                 validator: ValidatorInterface) -> None:
        """
        Args:
            conditions (List[ConditionInterface]):
                List of conditions stocks returned from scan should fulfill.
            stock_io (StockIoInterface, optional):
                An instance of StockIoInterface
            validator (ValidatorInterface, optional):
                A reference to a ValidatorInterface, the default is BasicValidator.
        """
        raise NotImplementedError()

    @abstractmethod
    def load_data(self, verbose: bool) -> "ScannerInterface":
        """
        Loads all stock data required for the scan.

        Args:
            verbose (bool, optional):
                Whether the download should be verbose, i.e. show progress or what
                stock is currently being downloaded.
        """
        pass

    @abstractmethod
    def get_candidates(self, at_day: datetime, verbose: bool) -> List[Stock]:
        """
        Return candidate stocks from the scan.

        Args:
            at_day (datetime)
            verbose (bool, optional):
                Whether the process should be verbose, i.e. show progress or what
                stock is currently being analyzed.
        """
        pass
