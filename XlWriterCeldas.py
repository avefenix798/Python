# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 14:25:14 2024

@author: Emmanuel
"""

import xlsxwriter

wb = xlsxwriter.Workbook('Hello.xlsx')

ws = wb.add_worksheet()

ws.write('A1', 123)
ws.write('A2', 23)
ws.write('A3', "=A1+A2")
ws.write('B3', "=MAX(A1:A2)")
wb.close()