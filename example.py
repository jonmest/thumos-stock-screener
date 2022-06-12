import datetime

from src.stock_scanner.condition.n_day_bullrun import NDayBullrun
from src.stock_scanner.condition.n_green_days import NGreenDays
from src.stock_scanner.scanner.BasicScanner import BasicScanner
from src.stock_scanner.stock_io import YahooIO

if __name__ == "__main__":
    path = f'./{YahooIO.valid_universes.NASDAQ.value}'

    print("Looking for consolidated stocks.")
    stock_io = YahooIO(YahooIO.valid_universes.NASDAQ, path)
    conditions = [NDayBullrun(window=3, min_bullrun_pct=0.1), NGreenDays(n_green_days=3)]


    start_date: datetime = datetime.datetime.now() - datetime.timedelta(days=30)
    end_date: datetime = datetime.datetime.now()
    candidates = BasicScanner(conditions, stock_io, start_date, end_date).get_candidates()
    print(list(map(lambda x: x.get_ticker(), candidates)))
