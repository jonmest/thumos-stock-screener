"""
This module defines the function for saving a list of stock tickers to a text file.
"""

import os
from datetime import datetime
from typing import List

from src.stock_scanner.stock.Stock import Stock


def saveTickersToFile(path: str, file_name: str, stocks: List[Stock]) -> None:
    """
    Saves a list of stock candidate tickers to a file.


    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    Parameters
    path: str
        Path to directory where the file should be saved
    file_name: str
        Name of file to be saved
    stocks: List[Stock]
        List of Stocks
    """
    with open(os.path.join(path, file_name), 'w') as file:
        now = datetime.now()
        file.write("Scan performed: " + now.strftime("%b %d, %Y %H:%M:%S") + "\n")
        for stock in stocks:
            file.write(f"{stock.get_ticker()}\n")
