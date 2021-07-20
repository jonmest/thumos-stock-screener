from ..condition.Condition import Condition
from ..Stock import Stock


class Consolidating(Condition):
    def __init__(self, window: int = 10, max_difference_percentage: int = 10) -> None:
        """
        In the constructor, implementations of this interface should be concerned with
        taking arguments defining the "rules" of the condition. In this instance, get values
        defining the rule "the stock's highest and lowest price during the last window days
        shall not be higher than max_difference_percentage".
        Args:
            stock (Stock)
        """
        super().__init__()
        self.window = window
        self.max_difference_percentage = max_difference_percentage


    def fulfilled(self, stock: Stock) -> bool:
        try:
            self.max_close = stock.getClose()[-self.window:].max()
            self.min_close = stock.getClose()[-self.window:].min()
        except IndexError:
            return False
        return self.min_close > self.max_close * (1 - (self.max_difference_percentage / 100))