# Parent class
from abc import ABC, abstractmethod
# Misc. for type hints
from typing import List

from src.stock_scanner.stock.Stock import Stock
from ..condition.Condition import Condition


class Validator(ABC):
    """
    Abstract Validator class
    What is a Validator?
    It essentially takes a stock, looks at the given conditions,
    and decides whether the stock should be returned as a scan candidate 
    or not.
    """

    def __init__(self, conditions: List[Condition]) -> None:
        """
        Parameters
        ----------
        conditions: List[Condition]
        """
        if conditions is None or len(conditions) < 1:
            raise ValueError('A list of Conditions needs to be supplied and can\t be empty')
        self.conditions: List[Condition] = conditions

    @abstractmethod
    def is_candidate(self, stock: Stock, **kwargs) -> bool:
        """
        Parameters
        ----------
        stock: Stock
        """
        if stock is None:
            raise ValueError('A Stock instance needs to be supplied.')
        return False
