#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 10:28:19 2018

@author: lytang
"""

from iexfinance import get_historical_data
from datetime import datetime
from iexfinance import get_available_symbols
stock_symbol = "BABA"

start = datetime(2017, 2, 9)
end = datetime(2017, 12, 24)

df = get_historical_data(stock_symbol, 
                         start=start, 
                         end=end, 
                         output_format='pandas')
# reformat and clean the data
df = df.reset_index()
df['date']=df['date'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d'))

# calculate return of data
import numpy as np
# df['close'].shift(1) # previous day closing price
df['return'] = np.log(df['close']/df['close'].shift(1))

df.head()

import pandas as pd
import matplotlib.pyplot as plt

window_length = 45

fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (10,5))
ax[0].plot(df['date'],df['close'])
ax[0].plot(df['date'],
        df['close'].rolling(window = window_length).mean(),
       linestyle=":")
# ax.plot(df['date'],df['low'])
ax[1].plot(df['date'],df['return'])
ax[1].plot(df['date'],
           df['return'].rolling(window = window_length).mean(),
          linestyle = '--')

for ax_ind in [0,1]:
    for tick in ax[ax_ind].get_xticklabels():
        tick.set_rotation(45)

ax[0].set_title("Stock opening prices for %s \n from %s to %s" \
             % (stock_symbol,
                str(datetime.date(start)),
                str(datetime.date(end))))

ax[1].set_title("Stock log(return) for \n %s \n from %s to %s" \
             % (stock_symbol,\
                str(datetime.date(start)),\
                str(datetime.date(end))))
