from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from pandas import Timestamp

from scanner import ScannerInterface
from stock.StockInterface import StockInterface

import traceback
import pprint


class BacktestCandidate:
    def __init__(self, stock: StockInterface, date: datetime, descriptive_statistics: dict):
        self.stock = stock
        self.date = date
        self.descriptive_statistics = descriptive_statistics

    def get_stock(self) -> StockInterface:
        return self.stock

    def get_date(self) -> datetime:
        return self.date

    def get_descriptive_statistics(self) -> dict:
        return self.descriptive_statistics

    def __str__(self) -> str:
        return self.stock.get_ticker() + " " + self.date.strftime("%Y-%m-%d") + " " + pprint.pformat(
            self.descriptive_statistics)

    def __repr__(self) -> str:
        return self.__str__()


class BacktestInterface:
    def __init__(self, scanner: ScannerInterface, from_date: datetime, to_date: datetime):
        self.scanner: ScannerInterface = scanner
        self.from_date = from_date
        self.to_date = to_date

    def load_data(self, verbose: bool = False):
        self.scanner.load_data(verbose)
        return self

    def run(self):
        dates = pd.date_range(start=self.from_date, end=self.to_date).tolist()
        candidates = []
        for current_datetime in dates:
            current_candidates = self.scanner.get_candidates(current_datetime)
            current_date = current_datetime.strftime("%Y-%m-%d")

            for item in current_candidates:
                try:
                    current_date_price = item.get_close().loc[current_date]
                    next_month_price = item.get_close().loc[current_date:][30]
                    chnge = ((next_month_price - current_date_price) / current_date_price)
                    backtest_candidate = BacktestCandidate(item, current_datetime, {"30 Day Performance": chnge})
                    candidates.append(backtest_candidate)
                except Exception:
                    continue

        return candidates
