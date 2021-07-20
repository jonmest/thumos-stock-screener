from ..condition.Condition import Condition
from ..Stock import Stock


class AboveTwoSMAs(Condition):
    """
    Example condition. Checks if a stock's current price
    is above two simple moving averages (SMAs).
    """
    def __init__(self, sma1_window: int = 150, sma2_period: int = 200) -> None:
        """
        In the constructor, implementations of this interface should be concerned with
        taking arguments defining the "rules" of the condition. In this instance, the 
        windows for computing two SMAs of the stock's close price.
        Args:
            stock (Stock)
        """
        super().__init__() # Always call super
        self.sma1_period = sma1_window
        self.sma2_period = sma2_period


    def fulfilled(self, stock: Stock) -> bool:
        """
        The method that determines whether the condition is fulfilled or not.
        """
        currentClose = stock.getClose()[-1]
        SMA1 = round(stock.getClose().rolling(window=self.sma1_period).mean(), 2)
        SMA2 = self.SMA150 = round(stock.getClose().rolling(window=self.sma2_period).mean(), 2)
        try:
            return currentClose > SMA1[-1] and currentClose > SMA2[-1]
        except IndexError:
            return False