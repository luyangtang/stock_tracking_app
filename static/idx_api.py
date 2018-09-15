#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 10:28:19 2018

@author: lytang
"""

class stock(object):
    
    # Initialisation
    #---------------
    
    def __init__(self,symbol):
        self.symbol = symbol
        
        
    # Repr
    #---------------
    
    def __repr__(self):
        return self.symbol
    
    
    # Get time series
    #----------------
    
    def get_data(self,start_date,end_date):
        
        '''
        start_date = '%d-%m-%Y'
        end_date = '%d-%m-%Y'
        returns a panda frame with date, volumn, open,
        high, low, close prices
        '''
        
        
        
        # parse the time
        #---------------
        
        from datetime import datetime
        from iexfinance import get_historical_data
        
        start_date_parsed = \
            datetime(int(start_date.split('-')[0]),\
                     int(start_date.split('-')[1]),\
                     int(start_date.split('-')[2]))
            
        end_date_parsed = \
            datetime(int(end_date.split('-')[0]),\
                     int(end_date.split('-')[1]),\
                     int(end_date.split('-')[2]))
            
        df = get_historical_data(self.symbol, 
                         start=start_date_parsed, 
                         end=end_date_parsed, 
                         output_format='pandas')
        
        return df.reset_index().to_json(orient='records')
        
        
        
#baba = stock('BABA')
#print(baba.get_data('01-08-2017','03-08-2017'))
