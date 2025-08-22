# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:00:58 2023

@author: Emmanuel
"""

import pandas as pd

datos = pd.DataFrame({'Ventas':[12,23],'Sucursla':['Mexico','toluca'] })


print(datos)
print ('total de ventas')
print(datos['Ventas'].sum())

datos.plot.bar('Sucursla' ,'Ventas')