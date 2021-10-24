"""
This module contains the abstract class defining the interface ALL 
DataReaders need to implement.
"""

import os
# Parent class
from datetime import datetime
from enum import Enum
from typing import List, Union

import pandas as pd
from yahoo_fin import stock_info as si
from yahooquery import Ticker

from .StockIoInterface import StockIoInterface
# Misc.
from src.stock_scanner.stock.Stock import Stock


class YahooIOValidUniverses(Enum):
    NASDAQ = "nasdaq"
    DOW = "dow"
    SP500 = "sp500"
    FTSE100 = "ftse100"
    FTSE250 = "ftse250"
    NIFTY50 = "nifty50"
    NIFTYBANK = "niftybank"


class YahooIO(StockIoInterface):
    """
    IO for Yahoo
    """
    valid_universes: YahooIOValidUniverses = YahooIOValidUniverses

    def __init__(self, universe: Union[str, YahooIOValidUniverses], path: str, max_tickers: int = None,
                 delimiter: str = None,
                 close_key: str = "adjclose", volume_key: str = "volume",
                 open_key: str = "open", high_key: str = "high",
                 low_key: str = "low", date_key: str = "date") -> None:
        """
        Args:
            universe (Union[str, YahooIOValidUniverses]): The name of the universe (one implementation could for example allow "nasdaq" or "sp500")
            path (str): The path to where the stock data should be downloaded.
            delimiter (str, optional): The delimiter used in the CSV files. 
                Can usually be left at default and automatically detected.      
            close_key (str, optional): Name of the column for the close value.
            volume_key (str, optional): Name of the column for the volume value.
            open_key (str, optional): Name of the column for the open value.
            high_key (str, optional): Name of the column for the high value.
            low_key (str, optional): Name of the column for the low value.
            date_key (str, optional): Name of the column for the date value.

        """
        if universe is None:
            raise ValueError('The name of a universe needs to be supplied. For example, \"^IXIC\" for NASDAQ stocks.')
        if path is None:
            raise ValueError('A path for where the stock data should be downloaded is required.')

        if not isinstance(universe, YahooIOValidUniverses):
            if universe not in [item.value for item in self.valid_universes]:
                raise ValueError("Invalid universe given.")
            self.universe = universe
        else:
            self.universe = universe.value

        if not os.path.exists(path):
            os.makedirs(path)

        self.path = path
        self.tickers = None
        self.max_tickers = max_tickers
        self.delimiter = delimiter
        self.close_key = close_key
        self.volume_key = volume_key
        self.open_key = open_key
        self.high_key = high_key
        self.low_key = low_key
        self.date_key = date_key

    def download_stock_data(self, start_date: datetime, end_date: datetime, verbose: bool = False) -> "YahooIO":
        """
        Downloading the data for stocks in the given the given universe.

        Args:
            start_date (datetime): From when should the data be downloaded (e.g. "let's download data from 2020-06-18")
            end_date (datetime): Until when should the data be downloaded (e.g. "let's download data from 2020-06-18 to 2021-06-18")
            verbose (bool, optional): Whether the download should be verbose, for example by displaying progress or which ticker is
                currently being downloaded. Handy for debugging purposes.
        """
        if not self.tickers:
            self.get_tickers()
        if self.max_tickers:
            tickers = self.tickers[:self.max_tickers]
        else:
            tickers = self.tickers

        for ticker in tickers:
            if verbose:
                print("Downloading data for ticker", ticker)
            df: pd.DataFrame = Ticker(ticker).history(start=start_date, end=end_date)
            try:
                df.to_csv(os.path.join(self.path, f"{ticker}.csv"))
            except Exception:
                if verbose:
                    print("Failed to save data for ticker", ticker)

        return self

    def read(self, ticker: str, start_date: datetime, end_date: datetime) -> Stock:
        """
        Read data from a ticker's file and return Stock.

        Args:
            ticker (str): Ticker of the stock.
            start_date (datetime)
            end_date (datetime)
        """
        path = self.__get_ticker_path__(ticker)
        df: pd.DataFrame = pd.read_csv(
            path, index_col=0, delimiter=self.delimiter
        )
        df['date'] = pd.to_datetime(df['date'])
        mask = (df['date'] > start_date) & (df['date'] <= end_date)
        df = df.loc[mask]
        stock: Stock = Stock(ticker, df, self.close_key,
                             self.volume_key, self.open_key, self.high_key,
                             self.low_key, self.date_key)
        return stock

    def __get_ticker_path__(self, ticker: str) -> str:
        """
        Return the path to the file for a stock.

        Args:
            ticker (str): Ticker for a stock (e.g. "AAPL")
        """
        return os.path.join(self.path, f"{ticker}.csv")

    def get_tickers(self) -> List[str]:
        """
        A convenient getter method for the ticker list.
        """
        if not self.tickers:
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

        if self.max_tickers:
            return self.tickers[:self.max_tickers]
        return self.tickers
