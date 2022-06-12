from ..stock.StockInterface import StockInterface
from ..condition.ConditionInterface import ConditionInterface


class NDayBullrun(ConditionInterface):
    def __init__(self, window: int = 10, min_bullrun_pct: float = 0.10) -> None:
        self.window = window
        self.min_bullrun_pct = min_bullrun_pct

    def fulfilled(self, stock: StockInterface) -> bool:
        try:
            first_close = stock.get_close()[-self.window]
            last_close = stock.get_close()[-1]
        except IndexError:
            return False
        abs_increase = last_close - first_close
        pct_increase = abs_increase / first_close
        return pct_increase >= self.min_bullrun_pct
