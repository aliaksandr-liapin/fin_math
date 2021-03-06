# -*- coding: utf-8 -*-
"""Stock Market Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gvHy5V-Re9VDZDydmFufzTNUaDh4yVtq

https://colab.research.google.com/
"""

import pandas
from pandas_datareader import DataReader

from datetime import datetime

stocks_list = ["FB",
               "AMZN",
               "NFLX",
               "GOOG"]

start = datetime(datetime.now().year - 1, 
                 datetime.now().month,
                 datetime.now().day)

end = datetime.now()

for stock in stocks_list:

  globals()[stock] = DataReader(stock,
                                "yahoo",
                                start,
                                end)

FB.describe()

print(AMZN)

NFLX.info()

GOOG["High"].plot()

GOOG["Volume"].plot(legend = True,
                    figsize = (14, 6))

moving_average_intervals = [5, 20, 50]

for moving_average in moving_average_intervals:

  column_name = "moving_average for %s days" %(str(moving_average))

  GOOG[column_name] = GOOG["Adj Close"].rolling(moving_average).mean()

GOOG[["Adj Close", 
      "moving_average for 5 days", 
      "moving_average for 20 days", 
      "moving_average for 50 days"]].plot(figsize=(14, 6))

GOOG["Daily Return"] = GOOG["Adj Close"].pct_change()

GOOG["Daily Return"].plot(figsize = (14, 14),
                          legend = True,
                          linestyle = '--',
                          marker = 'o')

adjusted_closing_dataframe = DataReader(stocks_list,
                            "yahoo",
                            start,
                            end)["Adj Close"]

print(adjusted_closing_dataframe)

adjusted_closing_dataframe.head()

stocks_returns = adjusted_closing_dataframe.pct_change()

print(stocks_returns)

import seaborn

seaborn.jointplot("GOOG", 
                  "GOOG",
                  data = stocks_returns,
                  color = "orange")

seaborn.jointplot("AMZN",
                  "NFLX",
                  data = stocks_returns)

seaborn.pairplot(data = stocks_returns.dropna())

returns_figure = seaborn.PairGrid(data = adjusted_closing_dataframe)

import matplotlib.pyplot as pyplot

returns_figure.map_upper(pyplot.scatter)

returns_figure.map_diag(pyplot.hist, bins = 30)

returns_figure.map_lower(seaborn.kdeplot)

print(stocks_returns.corr())

correlations = stocks_returns.corr()

seaborn.heatmap(data = correlations,
                fmt = "6g")

returns = stocks_returns.dropna()

import numpy

circles_area = numpy.pi * 15

pyplot.scatter(x = returns.mean(),
               y = returns.std(), 
               s = circles_area)

pyplot.xlabel("Expected Returns")

pyplot.ylabel("Risk")

for label, x, y in zip(returns.columns, 
                       returns.mean(), 
                       returns.std()):
  pyplot.annotate(label, 
                  xy = (x, y),
                  xytext = (50, 50),
                  textcoords = "offset points",
                  ha = "right",
                  va = "bottom",
                  arrowprops = dict(arrowstyle = "-",
                                    connectionstyle = "arc3, rad = -0.3"))

seaborn.distplot(GOOG["Daily Return"].dropna(),
                 bins = 100)

returns.head()

returns["FB"].quantile(0.05) * 100

returns["FB"].quantile(0.95) * 100