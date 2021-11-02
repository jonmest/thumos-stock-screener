from abc import ABC
from datetime import datetime
from typing import List

from src.stock_scanner.backtest.lib import BacktestCandidate
from src.stock_scanner.scanner.interfaces import ScannerInterface
from src.stock_scanner.backtest.interfaces import AnalyzerInterface


class BacktestInterface(ABC):
    def __init__(self, scanner: ScannerInterface, from_date: datetime, to_date: datetime,
                 analyzers: List[AnalyzerInterface]):
        raise NotImplementedError()

    def load_data(self, verbose: bool = False) -> "BacktestInterface":
        raise NotImplementedError()

    def run(self) -> List[BacktestCandidate]:
        raise NotImplementedError()
