# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 23:17:29 2022

@author: sepul
"""

import numpy as np 
import matplotlib.pyplot as plt



Datos= np.genfromtxt('./Datos_grosos_pelo.txt', skip_header=1) 

D= Datos[:,0]-7.5e-2
X=Datos[:,1]

plt.plot(D,X) #ta raro

d=640e-9/(np.sin(np.arctan(X/D))) 
Grosor=np.mean(d)

Delta_d= ((5e-3)*(640e-9)*(D)**2)/((X**2)+(D*2))**(3/2)+ ((5e-3)*(640e-9)*X*D)/((X**2)+(D**2))**(3/2)
Error=np.std(d)