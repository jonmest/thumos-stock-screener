from datetime import datetime
import os
from typing import List
from ..Stock import Stock

def saveTickersToFile (path: str, file_name: str, stocks: List[Stock]) -> None:
    """
    Saves a list of stock candidate tickers to a file.

    Parameters
    ----------
    path: str
        Path to where the file should be saved
    file_name: str
        Name of file to be saved
    stocks: List[Stock]
        List of Stocks
    """
    file = open(os.path.join(path, file_name), 'w')
    now = datetime.now()
    file.write("Scan performed: " + now.strftime("%b %d, %Y %H:%M:%S") + "\n")
    for stock in stocks:
        file.write(f"{stock.getTicker()}\n")
    file.close()