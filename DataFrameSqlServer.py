# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 22:22:38 2023

@author: Emmanuel
"""

import pyodbc
import pandas as pd
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'localhost' 
database = 'Northwind' 
username = 'sa' 
password = 'alejandra'  
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
# select 26 rows from SQL table to insert in dataframe.
query = "SELECT  c.CompanyName ,c.City ,c.Country  from Customers C;"
df = pd.read_sql(query, cnxn)
print(df)