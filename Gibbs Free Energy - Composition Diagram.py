# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 18:49:56 2021

@author: DSN Santosh
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import random
  
X = np.linspace(0, 1, 10000)
T = random.randint(100, 2000) #temperature in kelvin
S = -8.314*(X*np.log(X) + (1-X)*np.log(1 - X))
k = [-5,-3,-1,0,1,2,4,6,8,10] # interaction parameter
y0 =(-5)*X*(1-X)
y1 =(-3)*X*(1-X)
y2 =(-1)*X*(1-X)
y3 =(0)*X*(1-X)
y4 =(1)*X*(1-X)
y5 =(2)*X*(1-X)
y6 =(4)*X*(1-X)
y7 =(6)*X*(1-X)
y8 =(8)*X*(1-X)
y9 =(10)*X*(1-X)



g0 = y0 - T*S
g1 = y1 - T*S
g2 = y2 - T*S
g3 = y3 - T*S
g4 = y4 - T*S
g5 = y5 - T*S
g6 = y6 - T*S
g7 = y7 - T*S
g8 = y8 - T*S
g9 = y9 - T*S

print(T)

plt.plot(X, g0, color='b', label='k = -5')
plt.plot(X, g1, color='k', label='k = -3')
plt.plot(X, g2, color='y', label='k = -1')
plt.plot(X, g3, color='c', label='k = 0')
plt.plot(X, g4, color='b', label='k = 1')
plt.plot(X, g5, color='g', label='k = 2')
plt.plot(X, g6, color='b', label='k = 4')
plt.plot(X, g7, color='m', label='k = 6')
plt.plot(X, g8, color='r', label='k = 8')
plt.plot(X, g9, color='b', label='k = 10')




plt.xlabel("Mole Fraction")
plt.ylabel("Excess Gibbs Free Energy")
plt.title("Free Energy - Composition Diagram")

plt.legend()
plt.show()