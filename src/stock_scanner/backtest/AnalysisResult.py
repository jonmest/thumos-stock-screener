import pprint
from typing import Iterable, Union, Any
from src.stock_scanner.stock.StockInterface import StockInterface


class AnalysisResult:
    def __init__(self, data: Any, description: str):
        self.data = data
        self.description = description

    def get_description(self) -> str:
        return self.description

    def get_data(self) -> Any:
        return self.data

    def __str__(self) -> str:
        return pprint.pformat({
            "Description:": self.description,
            "Data:": pprint.pformat(self.data)
        })

    def __repr__(self) -> str:
        return self.__str__()