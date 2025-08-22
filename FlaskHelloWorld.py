# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 09:56:19 2023

@author: Emmanuel
"""

from flask import Flask

app = Flask(__name__)



@app.route('/')
def index():
    return "Hello world"


app.run(host='0.0.0.0', port=81)