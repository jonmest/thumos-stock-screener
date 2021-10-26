# Parent class
from abc import ABC, abstractmethod

# Type hinting
from src.stock_scanner.stock.StockInterface import StockInterface


class ConditionInterface(ABC):
    """ Base class all other conditions must inherit from and implement methods for. """

    def __init__(self) -> None:
        """
        In the constructor, implementations of this interface should be concerned with
        taking arguments defining the "rules" of the condition. For example, the percentage
        a stock must have gone up in a given time frame to be considered fulfilling of the
        condition.
        """
        raise NotImplementedError()

    @abstractmethod
    def fulfilled(self, stock: StockInterface) -> bool:
        """
        The method checks if the condition is met for the
        given stock. Always take stock as an argument.
        """
        return False
