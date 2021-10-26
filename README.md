[![Tests pass](https://github.com/jonmest/stock-scanner/actions/workflows/gen-requirements.yml/badge.svg)](https://github.com/jonmest/stock-scanner/actions/workflows/gen-requirements.yml)[![DeepSource](https://deepsource.io/gh/jonmest/stock-scanner.svg/?label=active+issues&show_trend=true&token=BzPLQmQm-bonBbfeokcEkFu3)](https://deepsource.io/gh/jonmest/stock-scanner/?ref=repository-badge)

# stock-scanner
Rapidly develop your own stock scanners using this Python3 library.
- Built-in support for using the free Yahoo Finance API.
- Easily write your own conditions for deciding whether a stock should show up in your scan.
- Extensible and easily customizable - simply write your own implementations of the included interfaces.
## Example code
Using a pre-written example Condition:

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

## Core interfaces
The main goal of this library is to enable rapid stock scanner development and creation of modules that you simply swap in or out at will. To achieve this, there is a number of different interfaces (or more technically correct in Python, abstract classes):
- StockIOInterface - an interface for downloading stock data to disk and then reading it.
- ConditionInterface - an interface for checking whether a stock fulfills a condition. This is the interface you probably will be doing the most work with on your own, as it's the most crucial one when building a scanner.
- ValidatorInterface - an interface for deciding whether a stock should be returned as a candidate from the scan or not, given the conditions it fulfills.
- ScannerInterface - an interface for the "main engine" of the scan.
- StockInterface - an interface for interacting with the data of a stock.

## Basic use guidelines
1. Construct a StockIO instance.
2. Make a list of Condition instances.
3. Instantiate a Validator.
4. Pass these as arguments to a Scanner.

When using the included, basic implementations of some of these interfaces, the process is slightly simplified:
1. Construct a StockIO instance (for example, YahooIO)
2. Make a list of Condition instances.
3. Pass these as arguments to BasicScanner.

## Existing implementations of the interfaces
- YahooIO - fetches daily data from the open and free Yahoo Finance API. Works pretty well for many use cases, but there is a rate limit.
- BasicValidator - it looks at a stock and returns it as a candidate if it fulfills all given Conditions, otherwise not.
- BasicScanner - it runs the StockIO to download stock data, reads the data for each stock, and by default uses the BasicValidator to find candidates. It should suffice for most use cases where you look at a stock in isolation -- but if you want to make use of a Relative Strength Index, for instance, you may need to write your own logic in a custom implementation.

## Experimental
Currently, I'm working on a backtesting module to facilitate the analysis of the quality of a scanner. What if you could see the Win/Loss ratio of candidates in a scanner, the average return? Not yet done.

Moreover, there are some basic functions to export Stocks and their time series to interactive HTML/CSS/JS charts, PNG files, or writing a list of candidate tickers to a text file.
