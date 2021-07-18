# Parent class
from ..scanner.Scanner import Scanner

# Data IO
from ..data_reader.CSVReader import CSVReader
from ..data_reader.DataReader import DataReader
from ..data_fetcher.DataFetcher import DataFetcher
from ..data_fetcher.YahooDataFetcher import YahooDataFetcher

# Condition validation
from ..validator.Validator import Validator
from ..validator.BasicValidator import BasicValidator

# Misc.
import datetime
import traceback
from ..Stock import Stock
from typing import List
from ..condition.Condition import Condition


class BasicScanner(Scanner):
    def __init__(self, universe: str, conditions: List[Condition], 
                data_fetcher: DataFetcher = YahooDataFetcher, data_reader: DataReader = CSVReader,
                validator: Validator = BasicValidator
                ) -> None:
        super().__init__(universe, conditions, data_fetcher, data_reader, validator)

    def loadData(self, path: str, verbose: bool = False) -> None:
        start_date: datetime = datetime.datetime.now() - datetime.timedelta(days=365)
        end_date: datetime = datetime.date.today()

        self.data_fetcher = self.data_fetcher(self.universe, path, verbose)
        self.data_fetcher.downloadTickers()
        self.data_fetcher.downloadStockData(start_date, end_date)

    def getCandidates(self, verbose: bool = False) -> List[Stock]:
        condition_validator: Validator = self.validator(self.conditions)
        self.data_reader = self.data_reader()
        candidates: List[Stock] = []
        
        for ticker in self.data_fetcher.getTickers():    
            try:
                stock: Stock = self.data_reader.read(ticker, self.data_fetcher.getTickerPath(ticker))
                
                if condition_validator.allFulfilled(stock):
                    candidates.append(stock)

            except Exception as e:
                if verbose:
                    print("Failed to analyze stock {ticker}: {e}")
                    traceback.print_exc()
        
        return candidates