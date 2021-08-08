from stock_scanner import Stock
from stock_scanner.condition import Condition
from stock_scanner.condition.Consolidating import Consolidating
from stock_scanner.scanner.BasicScanner import BasicScanner
from stock_scanner.io import YahooIO
import os

universe = 'nasdaq'
path = f'./{universe}'

print("Looking for consolidated stocks.")

stock_io = YahooIO(universe, path, max_tickers=50)
conditions = [ Consolidating(window=10, max_difference_percentage=5) ]

candidates = (
            BasicScanner(conditions, stock_io)
                .loadData()
                .getCandidates()
)

print(list(map(lambda x: x.getTicker(), candidates)))


# You can simply create your own conditions like this:
class AboveTwoSMAs(Condition):
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
        super().__init__() # Always call super
        self.sma1_period = sma1_period
        self.sma2_period = sma2_period


    def fulfilled(self, stock: Stock) -> bool:
        """
        The method that determines whether the condition is fulfilled or not.
        
        Args:
            stock (Stock)
        """
        currentClose = stock.getClose()[-1]
        SMA1 = round(stock.getClose().rolling(window=self.sma1_period).mean(), 2)
        SMA2 = self.SMA150 = round(stock.getClose().rolling(window=self.sma2_period).mean(), 2)
        try:
            return currentClose > SMA1[-1] and currentClose > SMA2[-1]
        except IndexError:
            return False

print("Looking for consolidated stocks above the 150 and 200 SMA.")

conditions = [ AboveTwoSMAs(), Consolidating(window=10, max_difference_percentage=5) ]
candidates = (
            BasicScanner(conditions, stock_io)
                .loadData()
                .getCandidates()
)

print(list(map(lambda x: x.getTicker(), candidates)))