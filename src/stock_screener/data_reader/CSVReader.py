# Parent class
from ..data_reader.DataReader import DataReader

# Misc.
import pandas as pd
from ..Stock import Stock


class CSVReader(DataReader):
    """
    Abstract class for reading in stock OHLCV data from files
    saved by the YahooDataFetcher.
    """
    def __init__(self, delimiter: str = None, close_key: str = "adjclose",
                volume_key: str = "volume", open_key: str = "open", 
                high_key: str = "high", low_key: str = "low", date_key: str = "date") -> None:
        """
        Parameters
        ----------
        delimiter: str, optional
            The delimiter used in the CSV files. Can usually be left at default and automatically detected.
        close_key: str, optional
            Name of the column for the close value, default is compatible with YahooDataFetcher files. 
        volume_key: str, optional
            Name of the column for the volume value, default is compatible with YahooDataFetcher files. 
        open_key: str, optional
            Name of the column for the open value, default is compatible with YahooDataFetcher files. 
        high_key: str, optional
            Name of the column for the high value, default is compatible with YahooDataFetcher files. 
        low_key: str, optional
            Name of the column for the low value, default is compatible with YahooDataFetcher files.
        date_key: str, optional
            Name of the column for the date value, default is compatible with YahooDataFetcher files.
        """
        self.delimiter = delimiter
        self.close_key = close_key
        self.volume_key = volume_key
        self.open_key = open_key
        self.high_key = high_key
        self.low_key = low_key
        self.date_key = date_key

    def read(self, ticker: str, path: str) -> Stock:
        """
        Read data and return stock.

        Parameters
        ----------
        ticker: str
            Ticker of the stock
        path: str
            Path to stock's data file
        """
        df: pd.DataFrame = pd.read_csv(
            path, index_col=0, delimiter=self.delimiter
        )
        stock: Stock = Stock(ticker, df, self.close_key, 
            self.volume_key, self.open_key, self.high_key, 
            self.low_key, self.date_key)
        return stock