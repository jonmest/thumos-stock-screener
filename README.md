# Stock-scanner
Stock-scanner is a Python3 package aimed at facilitating the rapid development of custom stock scanners/screeners. The goal is for it to be a sort of framework which easily lets users swap different modules at their own discretion.

## Example code
Using a pre-written Condition:

```python
from stock_screener import Stock
from stock_screener.scanner import BasicScanner
from stock_screener.condition.Above150And200SMA import Above150And200SMA
from stock_screener.data_fetcher import YahooDataFetcher

universe = 'nasdaq'
path = f'./{universe}'

print("Looking for stocks above the 150 and 200 day SMA.")

data_fetcher = YahooDataFetcher(universe, path)
conditions = [ Above150And200SMA ]

candidates = (
            BasicScanner(conditions, data_fetcher)
                .loadData()
                .getCandidates()
)

print(list(map(lambda x: x.getTicker(), candidates)))
```
Writing a custom Condition:
```python
from stock_screener import Stock
from stock_screener.condition import Condition
from stock_screener.scanner.BasicScanner import BasicScanner
from stock_screener.data_fetcher.YahooDataFetcher import YahooDataFetcher

universe = 'nasdaq'
path = f'./{universe}'

# Has the stock consolidated?
class Consolidating(Condition):
    def __init__(self, stock: Stock) -> None:
        """
        Always call super in the constructor.
        """
        super().__init__(stock)

        # We will look from the last close to 10 days back
        window = 10
        try:
            # Find the max and min closes in this window
            self.max_close = stock.getClose()[-window:].max()
            self.min_close = stock.getClose()[-window:].min()
        except IndexError:
            return False

    def fulfilled(self) -> bool:
        """
        If the difference between them is less than 3%
        we consider the stock consolidated
        """
        return self.min_close > (self.max_close * 0.97)

print("Looking for consolidated stocks.")

data_fetcher = YahooDataFetcher(universe, path)
conditions = [ Above150And200SMA, Consolidating ]
candidates = (
            BasicScanner(conditions, data_fetcher)
                .loadData()
                .getCandidates()
)

print(list(map(lambda x: x.getTicker(), candidates)))
```

## Interfaces

To achieve this goal of modularity, the framework has a few different interfaces you need to implement when writing your own extensions. They are:

- DataFetcher - an interface for downloading stock data and saving it locally.
- DataReader - an interface for reading stock data files.
- Condition - an interface for checking whether a stock fulfills a condition.
- Validator - an interface for deciding whether a stock should be returned as a candidate from the scan or not, given the conditions it fulfills.
- Scanner - an interface for the "main engine" of the scan.

A general outline of the use of these interfaces could look as such:

1. Use a DataFetcher to download stock data.
2. Use a DataReader to load the stock data into memory.
3. Give a Validator a set of Conditions to see if the stock should be returned from the scan or not.

This process usually all takes place in a Scanner.

