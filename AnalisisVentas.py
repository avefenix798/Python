# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:16:48 2023

@author: Emmanuel
"""

import pandas as pd 

def main():
    datos = pd.DataFrame( { 'Ventas':[12.3,12,4 ] , 
                           
                           'Sucursal':['Toluca','Zinacantepec','Mexico']
                           
                           } )
    
    
    print(datos)
    
    
    datos.plot.bar('Sucursal','Ventas')
    print('Total de ventas')
    
    
    
    print(datos['Ventas'].sum())
    temp = datos.sort_values('Ventas',ascending= False )
    
    
    print('Mejores Sucursales en ventas')
    print(temp[:2])





if __name__ == "__main__":

    main()