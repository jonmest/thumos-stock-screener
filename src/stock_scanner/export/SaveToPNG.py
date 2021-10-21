import os
from datetime import date
from typing import List

import mplfinance as mpf
import pandas as pd

from src.stock_scanner.stock.Stock import Stock


def save_png(path: str, stocks: List[Stock], dpi=250):
    today = date.today().strftime("%b-%d-%Y")
    file_dir = os.path.join(path, today)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    for stock in stocks:
        location = os.path.join(file_dir, f"{stock.get_ticker()}.png")
        df = stock.get_dataframe()
        df[stock.date_key] = pd.to_datetime(df[stock.date_key])
        df = df.set_index(stock.date_key)

        mpf.plot(df, type='candle', volume=True,
                 savefig=dict(fname=f"{location}", dpi=dpi, pad_inches=0.25),
                 title=f"{stock.get_ticker()} {today}")
