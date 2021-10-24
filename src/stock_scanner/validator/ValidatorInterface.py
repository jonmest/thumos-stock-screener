# Parent class
from abc import ABC, abstractmethod
# Misc. for type hints
from typing import List

from src.stock_scanner.stock.Stock import Stock
from ..condition.ConditionInterface import ConditionInterface


class ValidatorInterface(ABC):
    """
    Abstract ValidatorInterface class
    What is a ValidatorInterface?
    It essentially takes a stock, looks at the given conditions,
    and decides whether the stock should be returned as a scan candidate 
    or not.
    """

    def __init__(self, conditions: List[ConditionInterface]) -> None:
        """
        Parameters
        ----------
        conditions: List[ConditionInterface]
        """
        raise NotImplementedError()

    @abstractmethod
    def is_candidate(self, stock: Stock, **kwargs) -> bool:
        """
        Parameters
        ----------
        stock: Stock
        """
        pass
