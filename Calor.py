# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:32:26 2021

@author: Emmanuel
"""


import matplotlib.pyplot as ptl 
import numpy as np 

ptl.figure()
datos = np.random.rand(20,20)
ptl.pcolormesh( datos , cmap ='hot')
ptl.show()


