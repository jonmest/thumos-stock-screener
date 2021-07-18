from data_fetcher.YahooDataFetcher import YahooDataFetcher
from condition.Above150And200SMA import Above150And200SMA
from condition.Consolidating import Consolidating
from data_reader.CSVReader import CSVReader
from scanner.BasicScanner import BasicScanner
from validator.BasicValidator import BasicValidator

index = 'nasdaq'
path = f'./{index}'

scanner = BasicScanner(index, [Above150And200SMA, Consolidating])
scanner.loadData(path)
candidates = scanner.getCandidates()

print(list(map(lambda x: x.getTicker(), candidates)))