from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from pandas import Timestamp

from scanner import ScannerInterface
from stock.StockInterface import StockInterface


class BacktestCandidate:
    def __init__(self, stock: StockInterface, date_showed_in_scan: datetime):
        self.stock = stock
        self.date_showed_in_scan = date_showed_in_scan

    def get_stock(self) -> StockInterface:
        return self.stock

    def get_date(self) -> datetime:
        return self.date_showed_in_scan


class BacktestInterface:
    def __init__(self, scanner: ScannerInterface, from_date: datetime, to_date: datetime):
        self.scanner: ScannerInterface = scanner
        self.from_date = from_date
        self.to_date = to_date

    def load_data(self, verbose: bool = False):
        self.scanner.load_data(verbose)
        return self

    def run(self):
        dates = pd.date_range(start=self.from_date, end=self.to_date).to_pydatetime().tolist()
        candidates = []
        for current_date in dates:

            current_candidates = self.scanner.get_candidates(current_date)
            for item in current_candidates:
                next_month = current_date.date() + timedelta(days=30)
                try:
                    current_date_price = item.get_close().loc[[current_date - timedelta(days=1)]].values[0]
                    next_month_price = item.get_close().loc[[next_month]].values[0]
                    print(next_month_price)
                    chnge = 100 * ((next_month_price - current_date_price) / current_date_price)
                    candidates.append({
                        "stock": item.ticker,
                        "current_date_price": current_date_price,
                        "30 day performance": next_month_price,
                        "date": current_date.date()
                    })
                except Exception as e:
                    print(e)
                    print("Failed :/")
        return candidates
