# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 18:05:53 2023

@author: Emmanuel
"""

import numpy as np #Librería numérica
import matplotlib.pyplot as plt # Para crear gráficos con matplotlib


from sklearn.linear_model import LinearRegression #Regresión Lineal con scikit-learn

def f(x):  # función f(x) = 0.1*x + 1.25 + 0.2*Ruido_Gaussiano
    np.random.seed(42) # para poder reproducirlo
    y = 0.1*x + 1.25 + 0.2*np.random.randn(x.shape[0])
    return y

x = np.arange(0, 20, 0.5) # generamos valores x de 0 a 20 en intervalos de 0.5
y = f(x) # calculamos y a partir de la función que hemos generado

# hacemos un gráfico de los datos que hemos generado
plt.scatter(x,y,label='data', color='red')
plt.title('Datos');
plt.show()


regresion_lineal = LinearRegression() # creamos una instancia de LinearRegression

# instruimos a la regresión lineal que aprenda de los datos (x,y)
regresion_lineal.fit(x.reshape(-1,1), y) 

# vemos los parámetros que ha estimado la regresión lineal
print('w = ' + str(regresion_lineal.coef_) + ', b = ' + str(regresion_lineal.intercept_))

# resultado: w = [0.09183522], b = 1.2858792525736682