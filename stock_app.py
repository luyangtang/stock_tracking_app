#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 20:42:51 2018

@author: lytang
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/index/')
def main(name = 'anna'):
    return render_template('index.html',name = name)



from wtforms import Form, StringField

class stock_search_form(Form):
    name = StringField('Name:')


@app.route('/login/', methods=['POST', 'GET'])
def login():
    form = stock_search_form(request.form)
    
    stock_symbol = request.form['name']
        
    return render_template('login.html',\
                           form = form,
                           result = stock_symbol)


