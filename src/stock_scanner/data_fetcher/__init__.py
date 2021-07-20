"""
Module for fetching the data for stocks later to be used in a scan. If you want to build your own custom
data fetcher for a certain API, for instance, you need to write a class that implements the interface
defined in `DataFetcher`.

However, there is the existing class `YahooDataFetcher` which should be plug-and-play, as it downloads
data from Yahoo's open finance API. It's not 100% reliable, but should suffice for use-cases where a
few false negatives is acceptable.
"""

from .DataFetcher import DataFetcher
from .YahooDataFetcher import YahooDataFetcher