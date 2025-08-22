# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 08:15:49 2024

@author: Usuario
"""

import pandas_gbq
import matplotlib.pyplot as ptl
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('Credencial.json')
project_id = "active-guild-346221"

sql = """
SELECT Cantidad , Precio FROM `active-guild-346221.Ventas.Manzanas` 
"""
df = pandas_gbq.read_gbq(sql, project_id=project_id, credentials=credentials)

print(df)

df.plot()

ptl.show()



