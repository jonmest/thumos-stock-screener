"""
Module for scanner classes that are concerned with the overarching
logic of performing a scan. If you want to build your own custom scanner,
you need to write a class that implements the interface defined in `Scanner`.

For rapid development of a basic scanner, on the other hand, `BasicScanner` should
be an ready-to-use class for many use-cases.
"""

from .BasicScanner import BasicScanner
from .Scanner import Scanner
