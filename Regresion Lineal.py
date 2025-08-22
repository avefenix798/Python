# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 18:44:01 2021

@author: Emmanuel
"""

from sklearn import datasets
from sklearn.linear_model import LinearRegression

dataset = datasets.load_boston()




objetivo = dataset['target']
independientes = dataset['data']




modelo = LinearRegression()
modelo.fit(X=independientes, y=objetivo)

predicciones = modelo.predict(independientes)


for y, y_pred in list(zip(objetivo, predicciones)) [:5]:
	print("Valor Real: {:.3f} Valor Estimado: {:.5f}".format(y, y_pred))

input()