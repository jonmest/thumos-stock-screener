from stock_scanner import Stock
from stock_scanner.condition import Condition
from stock_scanner.condition.Consolidating import Consolidating
from stock_scanner.scanner.BasicScanner import BasicScanner
from stock_scanner.condition.AboveTwoSMAs import AboveTwoSMAs
from stock_scanner.data_fetcher.YahooDataFetcher import YahooDataFetcher
import os

universe = 'nasdaq'
path = f'./{universe}'
os.environ['MAX_TICKERS'] = '50'

print("Looking for stocks above the 150 and 200 day SMA")

data_fetcher = YahooDataFetcher(universe, path)
conditions = [ Consolidating(window=10) ]

candidates = (
            BasicScanner(conditions, data_fetcher)
                .loadData()
                .getCandidates()
)

print(list(map(lambda x: x.getTicker(), candidates)))


# # You can simply create your own conditions like this:

# class Consolidating(Condition):
#     def __init__(self, stock: Stock) -> None:
#         """
#         Always call super in the constructor.
#         """
#         super().__init__(stock)

#         # We will look from the last close to 10 days back
#         window = 10
#         try:
#             # Find the max and min closes in this window
#             self.max_close = stock.getClose()[-window:].max()
#             self.min_close = stock.getClose()[-window:].min()
#         except IndexError:
#             return False

#     def fulfilled(self) -> bool:
#         """
#         If the difference between them is less than 3%
#         we consider the stock consolidated
#         """
#         return self.min_close > (self.max_close * 0.97)

# print("Looking for consolidated stocks.")

# conditions = [ Above150And200SMA, Consolidating ]
# candidates = (
#             BasicScanner(conditions, data_fetcher)
#                 .loadData()
#                 .getCandidates()
# )

# print(list(map(lambda x: x.getTicker(), candidates)))