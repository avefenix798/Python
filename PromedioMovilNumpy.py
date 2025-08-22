# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:59:33 2024

@author: Emmanuel
"""
import numpy as np 


def moving_average(x, w):
    return np.convolve(x, np.ones(w), "valid") / w


x = [10, 5, 8, 9, 15, 22, 26, 11, 15, 16, 18, 7]

data = np.array(x)



y = moving_average(data, 4)



print(x)

print(y) 