from ..stock.StockInterface import StockInterface
from ..condition.ConditionInterface import ConditionInterface


class NGreenDays(ConditionInterface):
    def __init__(self, n_green_days) -> None:
        self.n_green_days = n_green_days

    def fulfilled(self, stock: StockInterface) -> bool:
        if len(stock.get_close()) - 1 <= self.n_green_days:
            return False
        returns = (stock.get_close() - stock.get_close().shift(1)) / stock.get_close().shift(1)
        try:
            days = returns[-self.n_green_days:]
        except IndexError:
            return False
        for day in days:
            if day <= 0:
                return False
        return True
