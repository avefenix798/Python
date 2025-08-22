# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:51:54 2024

@author: Usuario
"""

# Import packages
from dash import Dash, html, dash_table
import pandas as pd

# Incorporate data
df =  pd.DataFrame({'Venta':[23,23,23]})
# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='Ventas diarias'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)