from datetime import datetime

from backtest.AnalysisResult import AnalysisResult
from backtest.AnalyzerInterface import AnalyzerInterface
from stock.StockInterface import StockInterface


class Performance30Days(AnalyzerInterface):
    def __init__(self):
        self.description: str = "The relative change of the stock's close price in 30 days since it showed up on scan."

    def get_result(self, stock:  StockInterface, in_scan_date: datetime) -> AnalysisResult:
        current_date: str = in_scan_date.strftime("%Y-%m-%d")
        current_date_price = stock.get_close().loc[current_date]
        next_month_price = stock.get_close().loc[current_date:][30]
        performance = ((next_month_price - current_date_price) / current_date_price)
        return AnalysisResult(performance, self.description)
