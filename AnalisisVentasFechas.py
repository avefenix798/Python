# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 21:34:55 2022

@author: Emmanuel
"""

import pandas as pd

datos = pd.read_csv('C:\Datos\Csv\Ventas.csv')
datos['year'] = pd.DatetimeIndex(datos['Fecha']).year
datos['month'] = pd.DatetimeIndex(datos['Fecha']).month

print(datos)
datos.plot('Fecha','Venta',title='Ventas por fecha')

print(datos)