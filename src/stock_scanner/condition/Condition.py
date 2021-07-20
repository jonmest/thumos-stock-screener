# Parent class
from abc import ABC, abstractmethod

# Type hinting
from ..Stock import Stock

class Condition(ABC):
    """ Base class all other conditions must inherit from and implement methods for. """
    def __init__(self, stock: Stock) -> None:
        """
        Args:
            stock (Stock):
                An instance of a Stock to check condition for.
        
        """
        if stock is None or not isinstance(stock, Stock):
            raise ValueError('A Stock instance needs to be supplied.')
        self.stock = stock
        

    @abstractmethod
    def fulfilled(self) -> bool:
        """
        The method checks if the condition is met for the
        supplied stock.
        """
        return False