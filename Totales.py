# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 18:42:23 2022

@author: Emmanuel
"""

import pandas as pd 

datos = pd.DataFrame({ 'Ventas':[12,34,23,34,45] ,
                      'Devoluciones':[2,3,4,12,2] 
                      })


datos['VentasPro'] = datos['Ventas']  * 1.5

datos.plot()

print(datos.sum())
print("El total de la suma es:")

print(datos['Ventas'] .sum())