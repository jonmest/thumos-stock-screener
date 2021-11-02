import datetime

from condition.lib.Consolidating import Consolidating
from scanner.lib.BasicScanner import BasicScanner
from src.stock_scanner.stock_io.lib import YahooIO

path = f'./{YahooIO.valid_universes.NASDAQ.value}'

print("Looking for consolidated stocks.")
stock_io = YahooIO(YahooIO.valid_universes.NASDAQ, path, max_tickers=50)
conditions = [Consolidating(window=10, max_difference_percentage=2)]

start_date: datetime = datetime.datetime.now() - datetime.timedelta(days=365)
end_date: datetime = datetime.datetime.now()
candidates = BasicScanner(conditions, stock_io, start_date, end_date).load_data().get_candidates()
print(list(map(lambda x: x.get_symbol(), candidates)))
