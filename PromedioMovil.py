# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:18:51 2024

@author: Emmanuel
"""

import numpy as np


def moving_average(x, w):
    return np.convolve(x, np.ones(w), "valid") / w


data = np.array([10, 5, 8, 9, 15, 22, 26, 11, 15, 16, 18, 7])

print(moving_average(data, 3))
