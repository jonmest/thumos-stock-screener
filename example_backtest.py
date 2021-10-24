import datetime

from src.stock_scanner.backtest.BacktestInterface import BacktestInterface
from src.stock_scanner.condition.Consolidating import Consolidating
from src.stock_scanner.scanner.BasicScanner import BasicScanner
from src.stock_scanner.stock_io import YahooIO

path = f'./{YahooIO.valid_universes.NASDAQ.value}'

print("Looking for consolidated stocks.")
stock_io = YahooIO(YahooIO.valid_universes.NASDAQ, path, max_tickers=50)
conditions = [Consolidating(window=10, max_difference_percentage=2)]

start_date: datetime = datetime.datetime.now() - datetime.timedelta(days=365)
end_date: datetime = datetime.datetime.now()
scanner = BasicScanner(conditions, stock_io, start_date, end_date)

candidates = BacktestInterface(scanner, start_date, end_date).run()

print(candidates)
