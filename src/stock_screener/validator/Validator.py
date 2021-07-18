# Parent class
from abc import ABC, abstractmethod

# Misc. for type hints
from typing import List
from Stock import Stock
from condition.Condition import Condition


"""
A base Validator class, which all validators should inherit from.
Any child class only needs to:
1. Call the super method in its constructor.
2. Provide a validation implementation of the "validation" method.
"""
class Validator(ABC):
    def __init__(self, conditions: List[Condition]) -> None:
        if conditions is None or len(conditions) < 1:
            raise ValueError('A list of Conditions needs to be supplied and can\t be empty')
        self.conditions: List[Condition] = conditions
    
    """
    The implementation of your validation should be made here.
    """
    @abstractmethod
    def validation(self, stock: Stock) -> bool:
        return False

    def allFulfilled(self, stock: Stock) -> bool:
        if stock is None:
            raise ValueError('A Stock instance needs to be supplied.')
        return self.validation(stock)