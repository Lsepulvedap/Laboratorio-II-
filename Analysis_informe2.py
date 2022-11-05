# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 16:34:54 2022

@author: sepul
"""

# Primero calculamos el índice de refracción sin el CD

import numpy as np
import matplotlib.pyplot as plt

Datos_1= np.genfromtxt('Libro1.txt', skip_header=1) #datos expermento sin cd
Datos_2= np.genfromtxt('Libro2.txt') #datos experimento con cd

incidente=np.array(Datos_1[:,0])*np.pi/180
refractado=np.array( Datos_1[:,1])*np.pi/180


plt.style.use('classic')
plt.plot(incidente, refractado)
plt.grid(True)
plt.xlabel('Ángulo incidente')
plt.ylabel('Ángulo refractado')



def f(x,y):
    return np.sin(x)/ np.sin(y)

n1= f(incidente, refractado)


delta_1= 0.05*(np.abs(np.cos(incidente)/np.sin(refractado)))+ 0.05*(np.abs((-1)*np.sin(incidente)*np.cos(refractado)/np.sin(refractado)**2))
Delta_1= np.mean(delta_1)

indice= np.mean(n1)
Std= np.std(n1)

#%% 

#Ahora calculamos con el cd 
#Conociendo el tamaño aproximado de los surcos  en metros
d= 1.4e-6 #metros
Delta_d= 3.4e-6 #error pequeño, pero la desviacion estándar es aun mas pequeña, en metros

#luego, podemos hallar el indice de refracción como 



D = np.array(Datos_2[:,0])*10**(-2)  #en metros                    
x = np.array(Datos_2[:,1])*10**(-2) #en metros
theta= x/D 
 


def n(theta):
    return 640e-9/(d*np.sin(np.arctan(x/D)))
      
               
n2= n(theta)

indice_2= np.mean(n2)
Std_2= np.std(n2)
















