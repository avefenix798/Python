# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 19:55:45 2023

@author: Emmanuel
"""

import pandas as pd 

ruta = r'‪C:\Datos\Csv\Ventas.csv'
ruta = ruta.strip("‪u202a")

print(ruta)
datos = pd.read_csv(ruta)
print('Total de ventas = ')
print(datos['Venta'].sum())