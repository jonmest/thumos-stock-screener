from src.stock_scanner.stock import Stock
from src.stock_scanner.condition import Condition
from src.stock_scanner.condition.Consolidating import Consolidating
from src.stock_scanner.scanner.BasicScanner import BasicScanner
from src.stock_scanner.stock_io import YahooIO
import os

universe = 'nasdaq'
path = f'./{universe}'

print("Looking for consolidated stocks.")

stock_io = YahooIO(universe, path, max_tickers=50)
conditions = [Consolidating(window=10, max_difference_percentage=5)]

candidates = (
    BasicScanner(conditions, stock_io)
    .load_data()
    .get_candidates()
)

print(list(map(lambda x: x.get_ticker(), candidates)))
