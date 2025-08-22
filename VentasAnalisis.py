# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:26:59 2024

@author: Emmanuel
"""

import pandas as pd 


Ventas = pd.DataFrame({'Maquina':['Maquina 1','Maquina 2','Maquina 3'] ,'Venta':[23,23,34] })

print(Ventas)

print(Ventas.describe())


Ventas.plot.bar('Maquina','Venta')

Ventas.plot('Maquina','Venta')