from datetime import date
import os
from typing import List

from ..Stock import Stock

import mplfinance as mpf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def saveToInteractive(path: str, stocks: List[Stock]):
    today = date.today().strftime("%b-%d-%Y")
    dir = os.path.join(path, today)
    if not os.path.exists(dir):
                os.makedirs(dir)
                
    for stock in stocks:
        ticker = stock.getTicker()
        location = os.path.join(dir, f"{stock.getTicker()}.html")

        fig = make_subplots(rows=2, cols=1, 
                        row_heights=[0.8, 0.2], shared_xaxes=True,
                        subplot_titles=(ticker, "Volume"))
        fig.add_trace(
            go.Candlestick(x=stock.getDate(),
                        open=stock.getOpen(),
                        high=stock.getHigh(),
                        low=stock.getLow(),
                        close=stock.getClose()
                        ),
            row=1, col=1
        )

        fig.add_trace(
            go.Bar(x=stock.getDate(), y=stock.getVolume()),
            row=2, col=1
        )
        fig.update_xaxes(
            rangebreaks=[
                dict(bounds=["sat", "mon"]), # Hide weekends
            ]
        )
        fig.write_html(location)