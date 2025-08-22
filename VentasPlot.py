# -*- coding: utf-8 -*-
"""
Created on Fri May 12 17:04:22 2023

@author: Emmanuel
"""

import pandas as pd 


Dat = pd.DataFrame({ 'Ventas':[12,34] , 'Dev':[1,2]   })
Dat['Real'] = Dat['Ventas'] -Dat['Dev']
Dat.plot()
print(Dat)