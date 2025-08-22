# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 18:04:39 2023

@author: Emmanuel
"""

import pandas as pd 



path = r"C:\Salidas\CategorySalesfor1997.txt"

datos = pd.read_csv( path)

datos = datos.sort_values(by = "CategorySales", ascending = False)

print(datos)
print("")
print ("Mejores Categorias")
print(datos[:3])

datos.plot.bar( x= 'CategoryName' , y = 'CategorySales' )