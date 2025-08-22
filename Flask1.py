# -*- coding: utf-8 -*-
"""
Created on Sun May 14 15:26:33 2023

@author: Emmanuel
"""

from flask import Flask 

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

app.run()
 
 
 

