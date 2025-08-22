# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 08:14:49 2024

@author: Usuario
"""
import xlsxwriter as xl 
def main():
    workbook =  xl.Workbook("Hello.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.name = "Trabajo"
    
    worksheet.write("A1","Hola mundo")
    
    worksheet.write("A2","Sistemas de informacion")
    
    
    worksheet = workbook.add_worksheet()
    worksheet.name = "Trabajo 2"
    
    worksheet.write("A1","Hola mundo")
    
    worksheet.write("A2","Sistemas de informacion")
    
    
    workbook.close()

if "__name__"== "__main__":
    main()