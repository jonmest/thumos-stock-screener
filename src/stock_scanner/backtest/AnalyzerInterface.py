from abc import ABC
from datetime import datetime

from ..backtest.AnalysisResult import AnalysisResult
from ..stock.StockInterface import StockInterface


class AnalyzerInterface(ABC):
    def get_result(self, stock:  StockInterface, in_scan_date: datetime) -> AnalysisResult:
        raise NotImplementedError()
