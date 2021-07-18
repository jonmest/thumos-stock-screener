import pandas as pd


class Stock:
    def __init__(self, ticker: str, df: pd.DataFrame, close_key: str = "Adj Close",
                volume_key: str = "Volume", open_key: str = "Open", 
                high_key: str = "High", low_key: str = "Low", date_key: str = "Date") -> None:
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

    def createSMA(self, window: int = 10) -> None:
        if not self.hasSMA(window):
            self._setSMA(window=window, sma=self.getSMA(window=window))

    def getSMA(self, window: int = 10) -> pd.Series:
        return round(self.df["Adj Close"].rolling(window=window).mean(), 2)

    def _setSMA(self, window: int, sma: pd.Series) -> None:
        self.df["SMA_"+str(window)] = sma

    def hasSMA(self, window: int) -> bool:
        return "SMA_"+str(window) in self.df