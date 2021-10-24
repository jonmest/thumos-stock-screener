import pandas as pd

from stock.StockInterface import StockInterface


class Stock(StockInterface):
    def __init__(self, ticker: str, df: pd.DataFrame, close_key: str = "adjclose",
                 volume_key: str = "volume", open_key: str = "open",
                 high_key: str = "high", low_key: str = "low", date_key: str = "date") -> None:
        self.ticker = ticker
        self.df = df
        self.close_key = close_key
        self.volume_key = volume_key
        self.open_key = open_key
        self.high_key = high_key
        self.low_key = low_key
        self.date_key = date_key

        if df.index.name != date_key:
            self.df = df.set_index(date_key)

    def get_close(self) -> pd.Series:
        return self.df[self.close_key]

    def get_volume(self) -> pd.Series:
        return self.df[self.volume_key]

    def get_open(self) -> pd.Series:
        return self.df[self.open_key]

    def get_low(self) -> pd.Series:
        return self.df[self.low_key]

    def get_high(self) -> pd.Series:
        return self.df[self.high_key]

    def get_date(self) -> pd.Series:
        return self.df[self.date_key]

    def get_ticker(self) -> str:
        return self.ticker

    def get_dataframe(self) -> pd.DataFrame:
        return self.df

    def has_column(self, name: str) -> bool:
        return name in self.df

    def set_column(self, name: str, column: pd.Series) -> None:
        self.df[name] = column

    def get_column(self, name: str) -> pd.Series:
        return self.df[name]

    def get_columns(self) -> pd.Index:
        return self.df.columns
