# Parent class
from abc import ABC, abstractmethod

# Type hinting
from ..Stock import Stock


"""
Base Condition class, which all other condition classes should inherit from.
"""
class Condition(ABC):
    def __init__(self, stock: Stock) -> None:
        if stock is None or not isinstance(stock, Stock):
            raise ValueError('A Stock instance needs to be supplied.')
        self.stock: Stock = stock

    """
    The method which checks if the condition is met for the
    supplied stock. Child classes should have their own
    implementation of this method.
    """
    @abstractmethod
    def fulfilled(self) -> bool:
        return False