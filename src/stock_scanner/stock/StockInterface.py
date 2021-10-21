import pandas as pd


class StockInterface:
    def __init__(self, ticker: str, df: pd.DataFrame, close_key: str,
                 volume_key: str, open_key: str,
                 high_key: str, low_key: str, date_key: str) -> None:
        pass

    def get_close(self) -> pd.Series:
        pass

    def get_volume(self) -> pd.Series:
        pass

    def get_open(self) -> pd.Series:
        pass

    def get_low(self) -> pd.Series:
        pass

    def get_high(self) -> pd.Series:
        pass

    def get_date(self) -> pd.Series:
        pass

    def get_ticker(self) -> str:
        pass

    def get_dataframe(self) -> pd.DataFrame:
        pass

    def has_column(self, name: str) -> bool:
        pass

    def set_column(self, name: str, column: pd.Series) -> None:
        pass

    def get_column(self, name: str) -> pd.Series:
        pass

    def get_columns(self) -> pd.Index:
        pass
