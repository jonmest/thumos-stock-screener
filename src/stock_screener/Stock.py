from typing import List
import pandas as pd


class Stock:
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

    def getClose(self) -> pd.Series:
        return self.df[self.close_key]

    def getVolume(self) -> pd.Series:
        return self.df[self.volume_key]

    def getOpen(self) -> pd.Series:
        return self.df[self.open_key]

    def getLow(self) -> pd.Series:
        return self.df[self.low_key]
    
    def getHigh(self) -> pd.Series:
        return self.df[self.high_key]

    def getDate(self) -> pd.Series:
        return self.df[self.date_key]

    def getTicker(self) -> str:
        return self.ticker
    
    def getDataFrame(self) -> pd.DataFrame:
        return self.df
    
    def hasColumn(self, name: str) -> bool:
        return name in self.df

    def setColumn(self, name: str, column: pd.Series) -> None:
        self.df[name] = column
    
    def getColumn(self, name: str) -> pd.Series:
        return self.df[name]

    def getColumns(self) -> List[str]:
        return self.df.columns