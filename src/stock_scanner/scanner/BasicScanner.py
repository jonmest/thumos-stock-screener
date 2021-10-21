# Parent class
# Misc.
import datetime
import traceback
from typing import List

from src.stock_scanner.stock.Stock import Stock
from ..condition.ConditionInterface import ConditionInterface
# Data IO
from ..stock_io.StockIoInterface import StockIoInterface
from ..scanner.ScannerInterface import ScannerInterface
from ..validator.BasicValidator import BasicValidator
# ConditionInterface validation
from ..validator.ValidatorInterface import ValidatorInterface


class BasicScanner(ScannerInterface):
    """
    Basic scanner class which should be sufficient for many use cases.
    Supply a list of conditions and it spits out the stocks conforming
    to them.
    You may want to write your own version for more advanced scans.
    """

    def __init__(self, conditions: List[ConditionInterface], stock_io: StockIoInterface,
                 validator: ValidatorInterface = None) -> None:
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

    def load_data(self, period: int = 365, verbose: bool = False) -> "BasicScanner":
        """
        Loads all stock data required for the scan.

        Args:
            period (int, optional):
                How many bars back you want data for each stock. The default
                is 365, so in that case you fetch daily data from now to
                365 bars back.
            verbose (bool, optional):
                Whether the download should be verbose, i.e. show progress or what
                stock is currently being downloaded.
        """
        start_date: datetime = datetime.datetime.now() - datetime.timedelta(days=period)
        end_date: datetime = datetime.datetime.now()

        self.stock_io.download_stock_data(start_date, end_date, verbose)
        return self

    def get_candidates(self, verbose: bool = False) -> List[Stock]:
        """
        Return candidate stocks from the scan.

        Args:
            verbose (bool, optional):
                Whether the process should be verbose, IE show progress or what
                stock is currently being analyzed.
        """
        candidates: List[Stock] = []

        for ticker in self.stock_io.get_tickers():
            try:
                stock: Stock = self.stock_io.read(ticker)

                if self.validator.is_candidate(stock):
                    candidates.append(stock)

            except Exception as e:
                if verbose:
                    print(f"Failed to analyze stock {ticker}: {e}")
                    traceback.print_exc()

        return candidates
