from ..condition.Condition import Condition
from ..Stock import Stock


class Above150And200SMA(Condition):
    """
    Example condition. Checks if a stock's current price
    is above its 150- and 200-day SMA.
    """
    def __init__(self, stock: Stock) -> None:
        """
        The constructor generally should be concerned with the attributes
        later used when assessing the truthhfulness of this condition being
        fulfilled.

        Parameters
        ----------
        stock: Stock
        """
        super().__init__(stock) # Always call super
        self.currentClose: float = stock.getClose()[-1]
        self.SMA150 = round(stock.getClose().rolling(window=150).mean(), 2)
        self.SMA200 = self.SMA150 = round(stock.getClose().rolling(window=200).mean(), 2)


    def fulfilled(self) -> bool:
        """
        The method that determines whether the condition is fulfilled or not.
        """
        try:
            return self.currentClose > self.SMA150[-1] and self.currentClose > self.SMA150[-1]
        except IndexError:
            return False