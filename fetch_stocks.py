import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas_datareader import DataReader
from datetime import datetime, date

stocks_list = ['AMZN', 'FB', 'GOOG']
start = datetime(datetime.now().year - 1, datetime.now().month, datetime.now().day)
end = datetime(datetime.now().year, datetime.now().month, datetime.now().day)

# 1. get data
"""
moving_average_intervals = [5, 20, 50]
for stock in stocks_list:
    globals()[stock] = DataReader(stock, 'yahoo', start, end)
    
plt.plot(GOOG['Close'])
plt.rcParams["figure.figsize"] = (16, 4)  
"""

# 2. set moving average
"""
for moving_average in moving_average_intervals:
    
    column = f'Moving average for {moving_average} days'
    GOOG[column] = GOOG['Adj Close'].rolling(moving_average).mean()
    plt.plot(GOOG[column])
"""

# 3. calculate daily prc change
"""
GOOG['Daily Return'] = GOOG['Adj Close'].pct_change()
plt.plot(GOOG['Daily Return'])
"""

# 4. Compare different assets
# using seaborn as sns for comparison - jointplot()/pairplot() + fb_goog_prices.dropna() - not implemented yet 
adjusted_closing_frame = pd.DataFrame(DataReader(stocks_list, 'yahoo', start, end)['Adj Close'])
daily_return = adjusted_closing_frame.pct_change()
fb_goog_prices = adjusted_closing_frame.iloc[:, 0:2]






# plt.show()

