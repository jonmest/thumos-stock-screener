from stock_screener.condition.Above150And200SMA import Above150And200SMA
from stock_screener.condition.Consolidating import Consolidating
from stock_screener.scanner import BasicScanner
index = 'nasdaq'
path = f'./{index}'

scanner = BasicScanner(index, [Above150And200SMA, Consolidating])
scanner.loadData(path)
candidates = scanner.getCandidates()

print(list(map(lambda x: x.getTicker(), candidates)))