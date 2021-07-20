from ..condition.Condition import Condition
from ..Stock import Stock


class Consolidating(Condition):
    def __init__(self, stock: Stock) -> None:
        """
        Always call super in the constructor.
        """
        super().__init__(stock)
        window = 10
        try:
            self.max_close = stock.getClose()[-window:].max()
            self.min_close = stock.getClose()[-window:].min()
        except IndexError:
            return False

    def fulfilled(self) -> bool:
        return self.min_close > (self.max_close * 0.9)