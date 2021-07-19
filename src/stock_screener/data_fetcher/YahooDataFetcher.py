# Parent class
from ..data_fetcher.DataFetcher import DataFetcher

# Misc.
import os
import pandas as pd
import yfinance as yf
from typing import List
from yahoo_fin import stock_info as si


class YahooDataFetcher(DataFetcher):
    def __init__(self, universe: str, path: str, verbose: bool = False) -> None:
        valid_universes: List[str] = ["nasdaq", "dow", "ftse100", "ftse250", "nifty50", "niftybank", "sp500"]
        if universe not in valid_universes:
            raise ValueError("Invalid universe given.")
        super().__init__(universe, path, verbose)

    def downloadTickers(self) -> None:
        if self.universe == "sp500":
            self.tickers = si.tickers_sp500()
        elif self.universe == "nasdaq":
            self.tickers = si.tickers_nasdaq()
        elif self.universe == "dow":
            self.tickers = si.tickers_dow()
        elif self.universe == "ftse100":
            self.tickers = si.tickers_ftse100()
        elif self.universe == "ftse250":
            self.tickers = si.tickers_ftse250()
        elif self.universe == "nifty50":
            self.tickers = si.tickers_nifty50()
        elif self.universe == "niftybank":
            self.tickers = si.tickers_niftybank()

        # Yahoo Finance uses dashes instead of dots
        self.tickers: List[str] = [item.replace(".", "-") for item in self.tickers]
        return self
    
    def getTickers(self) -> List[str]:
        return self.tickers[:100]

    def getTickerPath(self, ticker: str) -> str:
        return os.path.join(self.path, f"{ticker}.csv")

    def downloadStockData(self, start_date, end_date) -> None:
        for ticker in self.tickers[:100]:
            if self.verbose:
                print("Downloading data for", ticker)
            df: pd.DataFrame = yf.download(ticker, start_date, end_date, progress=self.verbose)
            df.to_csv(
                os.path.join(self.path, f"{ticker}.csv")
            )
        return self