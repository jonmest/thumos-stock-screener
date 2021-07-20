"""
Module for reading local stock files and returning Stock instances. If you want to build your own custom
data reader for a certain file format, you need to write a class that implements the interface
defined in `DataReader`.

However, there is the existing class `CSVReader` which should be plug-and-play when used in conjunction
with the YahooDataFetcher.
"""

from .CSVReader import CSVReader
from .DataReader import DataReader
