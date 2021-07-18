# Parent class
from abc import ABC, abstractmethod

# Misc.
from ..Stock import Stock


class DataReader(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def read(self, path: str) -> Stock:
        pass