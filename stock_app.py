#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 20:42:51 2018

@author: lytang
"""

from flask import Flask, render_template, request
from wtforms import Form, StringField

class stock_search_form(Form):
    name = StringField('Stock symbol:')
    
    

app = Flask(__name__)

@app.route('/index/', methods=['POST', 'GET'])
def main():
    form = stock_search_form(request.form)
    
    if request.method == 'POST':
        stock_symbol = request.form['name']
    else:
        stock_symbol = 'not selected'
    
    return render_template('index.html',\
                           form = form,
                           result = stock_symbol)



