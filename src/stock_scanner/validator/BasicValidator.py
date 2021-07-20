# Parent class
from ..validator.Validator import Validator

# Misc. for type hints
from typing import List
from ..Stock import Stock
from ..condition.Condition import Condition


class BasicValidator(Validator):
    """
    Basic validator class that only returns a stock
    as a candidate if ALL conditions are fulfilled.
    """
    def __init__(self, conditions: List[Condition]) -> None:
        """
        Parameters
        ----------
        conditions: List[Condition]
        """
        super().__init__(conditions)

    def validation(self, stock: Stock) -> bool:
        """
        Parameters
        ----------
        stock: Stock
        """
        for condition in self.conditions:
            if not condition.fulfilled(stock):
                return False
        return True
    