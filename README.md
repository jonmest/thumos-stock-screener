# Stock-scanner
Stock-scanner is a Python3 package aimed at facilitating the rapid development of custom stock scanners/screeners. The goal is for it to be a sort of framework which easily lets users swap different modules at their own discretion.

To achieve this, the framework has a few different interfaces you need to implement when writing your own extensions. They are:

## DataFetcher
DataFetcher is an interface for downloading stock data. The specifics 

#

- DataReader - an interface for reading stock data.
- Condition - an interface for checking whether a stock fulfills a condition in your scan.
- Validator - an interface for deciding whether a stock should be returned as a candidate from the scan or not, given the conditions it fulfills.
- Scanner - an interface for the "main engine" of the scan.

## Features
- 


[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)