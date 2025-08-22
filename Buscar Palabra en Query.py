# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:55:15 2020

@author: Emmanuel
"""
def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    for x in unique_list: 
        print (x) 

nombrearchivo = r'C:\Temp\dtsxsql\total.sql'
contenido=[]

with open(nombrearchivo) as fin:
    contenido = [ linea.strip().split(' ') for linea in fin ]

Local = [] 
for r in contenido:
    for x in r :
        Local.append(x)

unique(Local)