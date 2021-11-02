import datetime

from src.stock_scanner.backtest.lib import PerformanceNDays, BasicBacktest
from src.stock_scanner.condition.lib import Consolidating
from src.stock_scanner.scanner.lib import BasicScanner
from src.stock_scanner.stock_io.lib import YahooIO

path = f'./{YahooIO.valid_universes.NASDAQ.value}'

# Use the same scanner as in example.py
stock_io = YahooIO(YahooIO.valid_universes.NASDAQ, path, max_tickers=20)
conditions = [Consolidating(window=10, max_difference_percentage=2)]
start_date: datetime = datetime.datetime.now() - datetime.timedelta(days=600)
end_date: datetime = datetime.datetime.now()

scanner = BasicScanner(conditions, stock_io, start_date, end_date)

candidates = BasicBacktest(scanner, start_date, end_date, [PerformanceNDays(period=30)]).run()

print(candidates)
