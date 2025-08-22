# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 09:36:04 2024

@author: Usuario
"""

import pandas as pd

archivo = r'C:\Datos\Csv\SSIS\Sales.txt'

datos = pd.read_csv(archivo , index_col=0, encoding='latin-1')

print(datos)
print('')
print('Total de Ventas ')

print(datos['ProductSales'].sum())

datos.plot('ProductName' , 'ProductSales')

