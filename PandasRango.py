# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 17:45:20 2021

@author: Emmanuel
"""
import pandas as pd
import pandasql as ps
import numpy as np 

df = pd.DataFrame([[1234, 'Customer A', '123 Street', np.nan],
               [1234, 'Customer A', np.nan, '333 Street'],
               [1233, 'Customer B', '444 Street', '333 Street'],
              [1233, 'Customer B', '444 Street', '666 Street']], columns=
['ID', 'Customer', 'Billing Address', 'Shipping Address'])

q1 = """SELECT sum(ID) Suma FROM df"""

print(ps.sqldf(q1, locals()))