# Parent class
from abc import ABC, abstractmethod

# Type hinting
from ..Stock import Stock

class Condition(ABC):
    """
    Base class all other Condition children inherit from.

    ...

    Methods
    -------
    fulfilled()
        Determines whether the condition is fulfilled for the current stock.
    """

    def __init__(self, stock: Stock) -> None:
        """
        Parameters
        ----------
        stock : Stock
            An instance of a Stock to check condition for
        """
        if stock is None or not isinstance(stock, Stock):
            raise ValueError('A Stock instance needs to be supplied.')
        self.stock: Stock = stock

    @abstractmethod
    def fulfilled(self) -> bool:
        """
        The method which checks if the condition is met for the
        supplied stock. Child classes should have their own
        implementation of this method.
        """
        return False