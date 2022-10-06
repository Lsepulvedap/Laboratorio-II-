# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 11:17:34 2022

@author: sepul
"""
#ctrl+1 para comentar
#shift+--> para seleccionar 

#Para cambiar de directorio uso cd nombre de la carpeta. No importa si tiene espacios; va sin 
#comillas, y cada carpeta se separa por doble backslash \\ 
import numpy as np 
import matplotlib.pyplot as plt

Datos= np.genfromtxt('./Datos_cd_storage.txt', skip_header=1) #./ me dice que estoy en esta carpeta


#GRAFICAMOS LOS DATOS
    
plt.scatter(Datos[:,0], Datos[:,1], color='blue') #Datos de la primera medición 
plt.scatter(Datos[:,3], Datos[:,4], color='green') #datos de la segunda medición



#En la primera y tercera toma de datos mantuve la línea en vertical, mientras que en la segunda toma 
#hice que los máximos se separaran en diagonal; observé que se cambiaba la orientación de los máximos
#a medida que alejaba el disco de la pantalla, por lo que fue mas difícil de medir

plt.style.use('classic')
plt.xlabel('Distancia a la pantalla [m]')
plt.ylabel('Separación entre los máximos [m]')
#plt.legend()
plt.grid()
plt.savefig("Experimento_1.jpg")
#-------------------------------------------------------------------------------------------------------

#CALCULAMOS LA DISTANCIA ENTRE LOS SURCOS'd' usando la fórmula d=\frac{\lambda}{\sin(\theta)}

#Supondremos que el disco está formado por cuadrados de lado d. D es la distancia a la pantalla

D_1=Datos[:,0]
D_2= Datos[:,3]

#Separación entre los máximos
x_1=Datos[:,1]
x_2=Datos[:,4]




d_1=640e-9/(np.sin(np.arctan(x_1/D_1))) #tamaño de los surcos
d_2=640e-9/(np.sin(np.arctan(x_2/D_2))) #// 

#CALCULAMOS AHORA EL ERROR PROPAGADO EN EL TAMAÑO DE LOS SURCOS

Delta_d_1= ((5e-3)*(640e-9)*(D_1)**2)/((x_1**2)+(D_1**2))**(3/2)+ ((5e-3)*(640e-9)*x_1)/((x_1**2)+(D_1**2))**(3/2)
Delta_d_2= ((5e-3)*(640e-9)*(D_2)**2)/((x_2**2)+(D_2**2))**(3/2)+ ((5e-3)*(640e-9)*x_2)/((x_2**2)+(D_2**2))**(3/2)

#El error obtenido antes es muy pequeño, así que hay que buscar otra forma de calcular unu 

#CALCULAMOS AHORA LA CAPACIDAD DEL DISCO EN BYTES

R, Delta_R= 6e-2, 5e-3 #Delta_R=Delta_r=Delta_x=Delta_D
r=2e-2

N_1=(np.pi/8)*(R**2-r**2)/(d_1)**2 #--> me entrega un valor para cada elemento de d_i
N_2=(np.pi/8)*(R**2-r**2)/(d_2)**2



#AHORA, LA CAPACIDAD DEL DISCO SERÁ EL PROMEDIO DE N_1 Y N_3, POR LO QUE EL ERROR ASOCIADO
#A ELLO SE DEBE CALCULAR TOMANDO ESTO EN CUENTA


#Luego, la capacidad del CD en megabites ¿'megabits'?
#Usamos este arreglo para ver el error total, esto es, con la desviación estándar

N=[N_1/1e6,N_2/1e6] 
Mean_N=np.mean(N)
Std= np.std(N)

#Luego, para entregar un valor, entregamos el valor promedio de los datos de la capacidad y el error 
#asociado a este es la desviación estándar



#Notas y dudas para mi unu



#DUDA: si tengo un valor para cada N_i, al calcular el promedio de N_i obtengo un número, pero si quiero
#el promedio de tooooodos los datos que obtuve, tengo que hacer el 'promedio del promedio' de los N_i
#¿ No hay otra forma mas fácil?

#OTRA DUDA: Si la desviación estándar de los datos me retorna la 'separación' entre cada dato
# me sirve realmente para hallar el error de la medición? Quizá sea mejor usar la formulita de 
#propagación de errores.. quizá en python ya está programada





