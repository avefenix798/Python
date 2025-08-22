# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:01:37 2024

@author: Usuario
"""
import pyodbc
import pandas as pd
import matplotlib.pyplot as plt

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
def main():
    server = 'DESKTOP-KLQGNV9\SQLEXPRESS' 
    database = 'NORTHWND' 
    username = 'sa' 
    password = 'alejandra'  
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    # select 26 rows from SQL table to insert in dataframe.
    query = "select top 10 P.ProductName, P.ProductSales   \
    from [dbo].[Product Sales for 1997] P order by P.ProductSales  desc;"
    df = pd.read_sql(query, cnxn)
    df.plot.bar('ProductName','ProductSales')
    plt.title('Top 10 Ventas por categorias')
    plt.xlabel('Categorias')
    plt.ylabel('Ventas')
    plt.legend()
    plt.show()
    print('top 10 Productos mas Vendidos ')
    print(df)
    
    print('Total de suma Ventas')
    
    print(df['ProductSales'].sum())


if __name__ == "__main__":
    main()