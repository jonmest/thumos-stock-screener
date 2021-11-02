from abc import ABC
from datetime import datetime

from src.stock_scanner.backtest.AnalysisResult import AnalysisResult
from src.stock_scanner.stock.StockInterface import StockInterface


class AnalyzerInterface(ABC):
    def get_result(self, stock:  StockInterface, in_scan_date: datetime) -> AnalysisResult:
        raise NotImplementedError()
