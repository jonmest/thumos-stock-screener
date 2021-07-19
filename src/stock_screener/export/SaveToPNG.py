from datetime import date
import os
from typing import List

import pandas as pd
from ..Stock import Stock
import mplfinance as mpf

def saveToPNG(path: str, stocks: List[Stock], dpi=250):
    today = date.today().strftime("%b-%d-%Y")
    dir = os.path.join(path, today)
    if not os.path.exists(dir):
            os.makedirs(dir)

    for stock in stocks:
        location = os.path.join(dir, f"{stock.getTicker()}.png")
        df = stock.getDataFrame()
        df[stock.date_key] = pd.to_datetime(df[stock.date_key])
        df = df.set_index(stock.date_key)
        
        mpf.plot(df, type='candle', volume=True, 
                savefig=dict(fname = f"{location}", dpi = dpi, pad_inches = 0.25),
                title=f"{stock.getTicker()} {today}")