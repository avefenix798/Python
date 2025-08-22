# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 19:21:07 2023

@author: Emmanuel
"""

import pandas as pd 
ruta = r'‪Venta.csv'


datos = pd.read_csv(ruta.strip("‪u202a"))

print(datos) 
datos.plot('Fecha','Venta')

