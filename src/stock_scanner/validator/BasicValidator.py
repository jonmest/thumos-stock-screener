# Parent class
# Misc. for type hints
from typing import List

from src.stock_scanner.stock.Stock import Stock
from ..condition.ConditionInterface import ConditionInterface
from ..validator.ValidatorInterface import ValidatorInterface


class BasicValidator(ValidatorInterface):
    """
    Basic validator class that only returns a stock
    as a candidate if ALL conditions are fulfilled.
    """

    def __init__(self, conditions: List[ConditionInterface]) -> None:
        """
        Parameters
        ----------
        conditions: List[ConditionInterface]
        """
        if conditions is None or len(conditions) < 1:
            raise ValueError('A list of Conditions needs to be supplied and can\t be empty')
        self.conditions: List[ConditionInterface] = conditions

    def is_candidate(self, stock: Stock, **kwargs) -> bool:
        """
        Parameters
        ----------
        stock: Stock
        """
        for condition in self.conditions:
            if not condition.fulfilled(stock):
                return False
        return True
