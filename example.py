from stock_screener import Stock
from stock_screener.condition import Condition
from stock_screener.scanner.BasicScanner import BasicScanner
from stock_screener.condition.Above150And200SMA import Above150And200SMA
from stock_screener.data_fetcher.YahooDataFetcher import YahooDataFetcher

universe = 'nasdaq'
path = f'./{universe}'

print("Looking for stocks above the 150 and 200 day SMA")

data_fetcher = YahooDataFetcher(universe, path)
conditions = [ Above150And200SMA ]

candidates = (
            BasicScanner(conditions, data_fetcher)
                .loadData()
                .getCandidates()
)

print(list(map(lambda x: x.getTicker(), candidates)))


# You can simply create your own conditions like this:

class Consolidating(Condition):
    def __init__(self, stock: Stock) -> None:
        """
        Always call super in the constructor.
        """
        super().__init__(stock)

        # We will look from the last close to 10 days back
        window = 10
        try:
            # Find the max and min closes in this window
            self.max_close = stock.getClose()[-window:].max()
            self.min_close = stock.getClose()[-window:].min()
        except IndexError:
            return False

    def fulfilled(self) -> bool:
        """
        If the difference between them is less than 3%
        we consider the stock consolidated
        """
        return self.min_close > (self.max_close * 0.97)

print("Looking for consolidated stocks.")

candidates = (
            BasicScanner(conditions, data_fetcher)
                .loadData()
                .getCandidates()
)

print(list(map(lambda x: x.getTicker(), candidates)))