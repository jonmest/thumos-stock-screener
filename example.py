from src.stock_scanner.condition.Consolidating import Consolidating
from src.stock_scanner.scanner.BasicScanner import BasicScanner
from src.stock_scanner.stock_io import YahooIO

path = f'./{YahooIO.valid_universes.NASDAQ.value}'

print("Looking for consolidated stocks.")
stock_io = YahooIO(YahooIO.valid_universes.NASDAQ, path, max_tickers=50)
conditions = [Consolidating(window=10, max_difference_percentage=2)]
candidates = BasicScanner(conditions, stock_io).load_data().get_candidates()
print(list(map(lambda x: x.get_ticker(), candidates)))
