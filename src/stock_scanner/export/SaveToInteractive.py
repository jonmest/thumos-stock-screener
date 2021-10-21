import os
from datetime import date
from typing import List

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from src.stock_scanner.stock.Stock import Stock


def save_interactive(path: str, stocks: List[Stock]):
    today = date.today().strftime("%b-%d-%Y")
    file_dir = os.path.join(path, today)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    for stock in stocks:
        ticker = stock.get_ticker()
        location = os.path.join(file_dir, f"{stock.get_ticker()}.html")

        fig = make_subplots(rows=2, cols=1,
                            row_heights=[0.8, 0.2], shared_xaxes=True,
                            subplot_titles=(ticker, "Volume"))
        fig.add_trace(
            go.Candlestick(x=stock.get_date(),
                           open=stock.get_open(),
                           high=stock.get_high(),
                           low=stock.get_low(),
                           close=stock.get_close()
                           ),
            row=1, col=1
        )

        fig.add_trace(
            go.Bar(x=stock.get_date(), y=stock.get_volume()),
            row=2, col=1
        )
        fig.update_xaxes(
            rangebreaks=[
                dict(bounds=["sat", "mon"]),  # Hide weekends
            ]
        )
        fig.write_html(location)
