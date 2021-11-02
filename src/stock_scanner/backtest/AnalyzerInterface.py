from abc import ABC
from typing import Iterable, Union, Any

from src.stock_scanner.stock.StockInterface import StockInterface


class AnalysisResult:
    def __init__(self, stock: StockInterface, data: Any):
        self.stock = stock
        self.data = data

    def get_stock(self) -> StockInterface:
        return self.stock

    def get_data(self) -> Any:
        return self.data


class AnalyzerInterface(ABC):
    def get_result(self, stock:  StockInterface) -> AnalysisResult:
        raise NotImplementedError()
