from ..condition.Condition import Condition
from ..Stock import Stock


class Above150And200SMA(Condition):
    """
    Always call super in the constructor.
    """
    def __init__(self, stock: Stock) -> None:
        super().__init__(stock)
        self.currentClose: float = stock.getClose()[-1]
        stock.createSMA(150)
        stock.createSMA(200)
        self.stock: Stock = stock

    def fulfilled(self) -> bool:
        try:
            return self.currentClose > self.stock.getSMA(150)[-1] and self.currentClose > self.stock.getSMA(200)[-1]
        except IndexError:
            return False