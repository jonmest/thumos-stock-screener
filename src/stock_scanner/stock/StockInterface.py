import pandas as pd


class StockInterface:
    def __init__(self, ticker: str, df: pd.DataFrame, close_key: str,
                 volume_key: str, open_key: str,
                 high_key: str, low_key: str, date_key: str) -> None:
        raise NotImplementedError()

    def get_close(self) -> pd.Series:
        raise NotImplementedError()

    def get_volume(self) -> pd.Series:
        raise NotImplementedError()

    def get_open(self) -> pd.Series:
        raise NotImplementedError()

    def get_low(self) -> pd.Series:
        raise NotImplementedError()

    def get_high(self) -> pd.Series:
        raise NotImplementedError()

    def get_date(self) -> pd.Series:
        raise NotImplementedError()

    def get_ticker(self) -> str:
        raise NotImplementedError()

    def get_dataframe(self) -> pd.DataFrame:
        raise NotImplementedError()

    def has_column(self, name: str) -> bool:
        raise NotImplementedError()

    def set_column(self, name: str, column: pd.Series) -> None:
        raise NotImplementedError()

    def get_column(self, name: str) -> pd.Series:
        raise NotImplementedError()

    def get_columns(self) -> pd.Index:
        raise NotImplementedError()
