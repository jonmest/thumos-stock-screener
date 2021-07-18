# Parent class
from ..data_reader.DataReader import DataReader

# Misc.
import pandas as pd
from ..Stock import Stock


class CSVReader(DataReader):
    def __init__(self, delimiter: str = None, close_key: str = "Adj Close",
                volume_key: str = "Volume", open_key: str = "Open", 
                high_key: str = "High", low_key: str = "Low", date_key: str = "Date") -> None:
        self.delimiter = delimiter
        self.close_key = close_key
        self.volume_key = volume_key
        self.open_key = open_key
        self.high_key = high_key
        self.low_key = low_key
        self.date_key = date_key

    def read(self, ticker: str, path: str) -> Stock:
        df: pd.DataFrame = pd.read_csv(
            path, index_col=0, delimiter=self.delimiter
        )
        stock: Stock = Stock(ticker, df, self.close_key, 
            self.volume_key, self.open_key, self.high_key, 
            self.low_key, self.date_key)
        return stock