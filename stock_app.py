#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 20:42:51 2018

@author: lytang
"""

from flask import Flask, render_template, request
from wtforms import Form, StringField
from wtforms.fields.html5 import DateField
from static.idx_api import *

class stock_search_form(Form):
    name = StringField('Stock symbol:')
    start_date = DateField('Start date:', \
                           format = '%d-%m-%Y')
    end_date = DateField('End date:', \
                           format = '%d-%m-%Y')
    

app = Flask(__name__)

@app.route('/index/', methods=['POST', 'GET'])
def main():
    form = stock_search_form(request.form)
    
    
    # once getting the input, return the search values
    if request.method == 'POST':
        stock_symbol = request.form['name']
        
        required_stock = stock(stock_symbol)\
            .get_data(request.form['start_date'],\
                      request.form['end_date'])
        
    else:
        required_stock = 'not selected'
    
    return render_template('index.html',\
                           form = form,
                           result = required_stock)
    
    
#print(stock('BABA'))  

#stock_symbok = 'BABA'
#required_stock = stock(stock_symbol)
#print(required_stock.symbol)