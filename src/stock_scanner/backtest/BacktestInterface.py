from datetime import datetime, timedelta
from typing import List

import pandas as pd

from backtest.AnalysisResult import AnalysisResult
from src.stock_scanner.backtest.AnalyzerInterface import AnalyzerInterface
from scanner import ScannerInterface
from stock.StockInterface import StockInterface

import traceback
import pprint


class BacktestCandidate:
    def __init__(self, stock: StockInterface, date: datetime, analyses: List[AnalysisResult]):
        self.stock = stock
        self.date = date
        self.analyses = analyses

    def get_stock(self) -> StockInterface:
        return self.stock

    def get_date(self) -> datetime:
        return self.date

    def get_analyses(self) -> dict:
        return self.analyses

    def __str__(self) -> str:
        return self.stock.get_ticker() + " " + self.date.strftime("%Y-%m-%d") + " " + pprint.pformat(
            self.analyses)

    def __repr__(self) -> str:
        return self.__str__()


class BacktestInterface:
    def __init__(self, scanner: ScannerInterface, from_date: datetime, to_date: datetime, analyzers: List[AnalyzerInterface]):
        self.scanner: ScannerInterface = scanner
        self.from_date = from_date
        self.to_date = to_date
        self.analyzers = analyzers

    def load_data(self, verbose: bool = False):
        self.scanner.load_data(verbose)
        return self

    def run(self):
        dates = pd.date_range(start=self.from_date, end=self.to_date).tolist()
        candidates = []
        for current_datetime in dates:
            current_candidates = self.scanner.get_candidates(current_datetime)
            # current_date = current_datetime.strftime("%Y-%m-%d")

            for item in current_candidates:
                analyses: List[AnalysisResult] = []
                for analyzer in self.analyzers:
                    try:
                        analyses.append(analyzer.get_result(item, current_datetime))
                    except (KeyError, IndexError):
                        continue
                candidate: BacktestCandidate = BacktestCandidate(item, current_datetime, analyses)
                candidates.append(candidate)

                # try:
                #
                #     current_date_price = item.get_close().loc[current_date]
                #     next_month_price = item.get_close().loc[current_date:][30]
                #     chnge = ((next_month_price - current_date_price) / current_date_price)
                #     backtest_candidate = BacktestCandidate(item, current_datetime, {"30 Day Performance": chnge})
                #     candidates.append(backtest_candidate)
                # except Exception:
                #     continue

        return candidates
