from src.stock_scanner.stock.StockInterface import StockInterface
from ..condition.ConditionInterface import ConditionInterface


class Consolidating(ConditionInterface):
    def __init__(self, window: int = 10, max_difference_percentage: int = 10) -> None:
        """
        In the constructor, implementations of this interface should be concerned with
        taking arguments defining the "rules" of the condition. In this instance, get values
        defining the rule "the stock's highest and lowest price during the last window days
        shall not be higher than max_difference_percentage".
        Args:
            stock (StockInterface)
        """
        self.window = window
        self.max_difference_percentage = max_difference_percentage

    def fulfilled(self, stock: StockInterface) -> bool:
        try:
            max_close = stock.get_close()[-self.window:].max()
            min_close = stock.get_close()[-self.window:].min()
        except IndexError:
            return False
        return min_close > max_close * (1 - (self.max_difference_percentage / 100))
