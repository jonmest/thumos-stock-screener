# Parent class
# Misc.
from datetime import datetime
import traceback
from typing import List

from src.stock_scanner.stock.Stock import Stock
from src.stock_scanner.condition.ConditionInterface import ConditionInterface
# Data IO
from src.stock_scanner.stock_io.StockIoInterface import StockIoInterface
from src.stock_scanner.scanner.ScannerInterface import ScannerInterface
from src.stock_scanner.validator.BasicValidator import BasicValidator
# ConditionInterface validation
from src.stock_scanner.validator.ValidatorInterface import ValidatorInterface


class BasicScanner(ScannerInterface):
    """
    Basic scanner class which should be sufficient for many use cases.
    Supply a list of conditions and it spits out the stocks conforming
    to them.
    You may want to write your own version for more advanced scans.
    """

    def __init__(self, conditions: List[ConditionInterface], stock_io: StockIoInterface,
                 start_date: datetime, end_date: datetime, validator: ValidatorInterface = None) -> None:
        """
        Args:
            conditions (List[ConditionInterface]):
                List of conditions stocks returned from scan should fulfill.
            stock_io (StockIoInterface):
                An instance of StockIoInterface.
            validator (ValidatorInterface):
                A reference to a Validator, the default is BasicValidator.
        """
        if validator is None:
            validator = BasicValidator(conditions)
        self.conditions: List[ConditionInterface] = conditions
        self.stock_io: StockIoInterface = stock_io
        self.validator: ValidatorInterface = validator
        self.start_date = start_date
        self.end_date = end_date

    def load_data(self, verbose: bool = False) -> "BasicScanner":
        """
        Loads all stock data required for the scan.

        Args:
            start_date (datetime)
            end_date (datetime)
            verbose (bool, optional):
                Whether the download should be verbose, i.e. show progress or what
                stock is currently being downloaded.
        """

        self.stock_io.download_stock_data(self.start_date, self.end_date, verbose)
        return self

    def get_candidates(self, at_day: datetime = None, verbose: bool = False) -> List[Stock]:
        """
        Return candidate stocks from the scan.

        Args:
            verbose (bool, optional):
                Whether the process should be verbose, IE show progress or what
                stock is currently being analyzed.
        """
        if at_day is None:
            at_day = self.end_date

        candidates: List[Stock] = []

        for ticker in self.stock_io.get_tickers():
            try:
                stock: Stock = self.stock_io.read(ticker, self.start_date, at_day)

                if self.validator.is_candidate(stock):
                    candidates.append(self.stock_io.read(ticker, self.start_date, self.end_date))

            except Exception as e:
                if verbose:
                    print(f"Failed to analyze stock {ticker}: {e}")
                    traceback.print_exc()

        return candidates
