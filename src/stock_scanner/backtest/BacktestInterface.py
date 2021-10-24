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
            print("HEJ")
            for item in current_candidates:
                next_month = Timestamp(current_date + timedelta(days=30))
                if next_month in item.get_close().index.values:
                    print("In here")
                    current_date_price = item.get_close()
                    next_month_price = item.get_close().iloc(current_date + timedelta(days=30))
                    chnge = 100 * ((next_month_price - current_date_price) / current_date_price)
                    candidates.append({
                        "stock": item,
                        "30 day performance": chnge
                    })
        return candidates
