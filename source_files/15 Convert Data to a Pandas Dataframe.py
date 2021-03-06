# -*- coding: utf-8 -*-
"""Build an Equal-Weight S&P 500 Index Fund.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zVAguryCfEjqGaN75WkMlZDNG7SSYJGu

https://colab.research.google.com/
"""

import requests 

symbol = "GOOG"

IEX_CLOUD_API_TOKEN = "Tpk_303eba2884a34a0e937ec42ab848532a"

api_url = f"https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}"

data = requests.get(api_url).json()

print(data)

data

import pandas

page = pandas.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")

print(page)

stocks_table = page[0]

print(stocks_table)

stocks_table.info()

stocks_columns = ["Ticker", "Price", "Market Capitalization", "Shares to Buy"]

stocks_dataframe = pandas.DataFrame(columns = stocks_columns)

for symbol in stocks_table["Symbol"]:

  api_url = f"https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}"

  data = requests.get(api_url).json()

  stocks_dataframe = stocks_dataframe.append(pandas.Series([symbol,
                                                            data["latestPrice"],
                                                            data["marketCap"],
                                                            "N/A"],
                                                           index = stocks_columns),
                                             ignore_index = True)
  
print(stocks_dataframe)