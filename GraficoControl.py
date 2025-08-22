# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:19:21 2024

@author: Emmanuel
"""

import pandas as pd 
import matplotlib.pyplot as ptl


datos = pd.DataFrame({'Medidas':[23.3,23,23,24,22,23.45]})


datos['Inferior'] = datos['Medidas'].min()
datos['Superior'] = datos['Medidas'].max()
datos['Promedio'] = datos['Medidas'].mean()


datos.plot(title='Grafico de Control')
ptl.show()