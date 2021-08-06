from typing import List
import pandas as pd

class Stock:
    def __init__(self, ticker: str, df: pd.DataFrame, close_key: str = "adjclose",
                volume_key: str = "volume", open_key: str = "open", 
                high_key: str = "high", low_key: str = "low", date_key: str = "date") -> None:
        self._ticker = ticker
        self._df = df
        self._close_key = close_key
        self._volume_key = volume_key
        self._open_key = open_key
        self._high_key = high_key
        self._low_key = low_key
        self._date_key = date_key

    def getClose(self) -> pd.Series:
        return self._df[self._close_key]

    def getOpen(self) -> pd.Series:
        return self._df[self._open_key]

    def getLow(self) -> pd.Series:
        return self._df[self._low_key]
    
    def getHigh(self) -> pd.Series:
        return self._df[self._high_key]

    def getDate(self) -> pd.Series:
        return self._df[self._date_key]
    
    def getVolume(self) -> pd.Series:
        return self._df[self._volume_key]

    def getTicker(self) -> str:
        return self._ticker
    
    def getDataFrame(self) -> pd.DataFrame:
        return self._df
    
    def hasColumn(self, name: str) -> bool:
        return name in self._df

    def setColumn(self, name: str, column: pd.Series) -> None:
        self._df[name] = column
    
    def getColumn(self, name: str) -> pd.Series:
        return self._df[name]

    def getColumns(self) -> List[str]:
        return self._df.columns
