# Parent class
from validator.Validator import Validator

# Misc. for type hints
from typing import List
from Stock import Stock
from condition.Condition import Condition


class BasicValidator(Validator):
    """
    Constructor, always call super.
    """
    def __init__(self, conditions: List[Condition]) -> None:
        super().__init__(conditions)

    """
    An example validation implementation. For this method to return True,
    all conditions need to be True.
    """
    def validation(self, stock: Stock) -> bool:
        for condition in self.conditions:
            if not condition(stock).fulfilled():
                return False
        return True
    