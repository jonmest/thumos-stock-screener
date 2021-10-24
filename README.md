# stock-scanner
Stock-scanner is a Python3 package aimed at facilitating the rapid development of custom stock scanners/screeners. The goal is for it to be a sort of framework which easily lets users swap different modules at their own discretion.

## Example code
Using a pre-written Condition:

```python
from src.stock_scanner.condition.Consolidating import Consolidating
from src.stock_scanner.scanner.BasicScanner import BasicScanner
from src.stock_scanner.stock_io import YahooIO

path = f'./{YahooIO.valid_universes.NASDAQ.value}'

print("Looking for consolidated stocks.")
stock_io = YahooIO(YahooIO.valid_universes.NASDAQ, path, max_tickers=50)
conditions = [Consolidating(window=10, max_difference_percentage=2)]
candidates = BasicScanner(conditions, stock_io).load_data().get_candidates()
print(list(map(lambda x: x.get_ticker(), candidates)))
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

