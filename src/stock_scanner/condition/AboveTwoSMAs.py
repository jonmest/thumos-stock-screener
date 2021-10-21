from src.stock_scanner.stock.Stock import Stock
from ..condition.ConditionInterface import ConditionInterface


class AboveTwoSMAs(ConditionInterface):
    """
    Example condition. Checks if a stock's current price
    is above two simple moving averages (SMAs).
    """

    def __init__(self, sma1_period: int = 150, sma2_period: int = 200) -> None:
        """
        In the constructor, implementations of this interface should be concerned with
        taking arguments defining the "rules" of the condition. In this instance, the 
        windows for computing two SMAs of the stock's close price.
        Args:
            sma1_period (int)
            sma2_period (int)
        """
        super().__init__()  # Always call super
        self.sma1_period = sma1_period
        self.sma2_period = sma2_period

    def fulfilled(self, stock: Stock) -> bool:
        """
        The method that determines whether the condition is fulfilled or not.
        
        Args:
            stock (Stock)
        """
        current_close = stock.get_close()[-1]
        sma1 = round(stock.get_close().rolling(window=self.sma1_period).mean(), 2)
        sma2 = round(stock.get_close().rolling(window=self.sma2_period).mean(), 2)
        try:
            return current_close > sma1[-1] and current_close > sma2[-1]
        except IndexError:
            return False
