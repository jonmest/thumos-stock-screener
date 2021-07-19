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
    """
    Basic scanner class which should be sufficient for many use cases. You make
    want to write your own version for more advanced scans.
    """
    def __init__(self, conditions: List[Condition], 
                data_fetcher: DataFetcher = YahooDataFetcher, data_reader: DataReader = CSVReader,
                validator: Validator = BasicValidator
                ) -> None:
        """
        Parameters
        ----------
        conditions: List[Condition]
            List of conditions stocks returned from scan should fulfill.
            An instance of DataFetcher, default is YahooDataFetcher.
        data_reader: DataReader, optional
            An instance of DataReader, the default is CSVReader and is compatible with
            files saved by YahooDataFetcher.
        validator: Validator, optional
            An instance of Validator, the default is BasicValidator.
        """
        super().__init__(conditions, data_fetcher, data_reader, validator)

    def loadData(self, verbose: bool = False) -> None:
        """
        Loads all stock data required for the scan.

        Parameters
        ----------
        path: str
            Path to where the data should be saved.
        verbose: bool, optional
            Whether the download should be verbose, IE show progress or what
            stock is currently being downloaded.
        """
        # Download two years of data for each stock
        start_date: datetime = datetime.datetime.now() - datetime.timedelta(days=730)
        end_date: datetime = datetime.date.today()

        self.data_fetcher.downloadTickers()
        self.data_fetcher.downloadStockData(start_date, end_date, verbose)
        return self

    def getCandidates(self, verbose: bool = False) -> List[Stock]:
        """
        Return candidate stocks from the scan.

        Parameters
        ----------
        verbose: bool, optional
            Whether the process should be verbose, IE show progress or what
            stock is currently being analyzed.
        """
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
                    print(f"Failed to analyze stock {ticker}: {e}")
                    traceback.print_exc()
        
        return candidates