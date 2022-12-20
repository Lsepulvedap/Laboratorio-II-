# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 11:58:14 2022

@author: sepul
"""
import numpy as np
import matplotlib.pyplot as plt 

#grafico de rho vs alpha
gamma= 0.2
alpha= np.linspace(0.01,1,100)
rho= gamma/alpha 


plt.style.use('bmh')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal')

plt.plot(alpha, rho)
ax.fill_between(alpha, rho, 1, color= 'blue', alpha= 0.1)

plt.grid(False)

plt.title('Densidad de población v/s tasa de activación')
plt.xlabel(r'Tasa de activación $\alpha$')
plt.ylabel( r'Densidad de población $\rho$' )

plt.text(0.6, 0.8, s= 'Actividad' )
plt.text(0.15, 0.2, s= 'Inactividad' ) 
plt.ylim(0,1)

plt.savefig('rho_vs_alpha.pdf')
#%% 
#Resolvemos la ecuacion con el método de Runke kutta de segundo orden

alpha= 0.5
gamma= 0.2 

def f(x,tiempo, rho): 
    return alpha* x* (rho- x)- gamma*x 

h=0.01
tiempo=np.arange(0,30, h)

x= np.zeros(tiempo.size)

for rho in np.linspace(0,1,10): 
    x[0]=0.1 
    
    for i in range(tiempo.size-1): 
        xmedio= x[i] + 0.5* h*f(x[i], tiempo[i], rho) 
        x[i+1] = x[i]+ h* f(xmedio, tiempo[i]+ 0.5*h, rho)
        
    plt.plot(tiempo, x, label= f'rho={rho: .1f}')
plt.legend()
plt.title('Hormigas activas en función del tiempo')
plt.xlabel('tiempo')
plt.ylabel(r'$x$') 
    
#%%
x, rho= np.mgrid[-0.001:1:500j, 0:1:500j]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal')


plt.grid(False)
plt.contour(rho, x ,f(x,tiempo, rho), levels=[0]) #grafica los puntos para los  cuales f(x,tiempo, rho)= levels =0 

#Flechas de arriba 
plt.arrow(0.13, 0.2, 0.0, -0.1, color= 'blue', head_width= 0.02)  
plt.arrow(0.26, 0.2, 0.0, -0.1, color= 'blue', head_width= 0.02)    
plt.arrow(0.4, 0.2, 0.0, -0.1, color= 'blue' , head_width= 0.02) 

plt.arrow(0.66, 0.43, 0.0, -0.1, color= 'blue', head_width= 0.02)  
plt.arrow(0.79, 0.6, 0.0, -0.1, color= 'blue', head_width= 0.02)    
plt.arrow(0.92, 0.8, 0.0, -0.1, color= 'blue', head_width= 0.02) 


#Flechas de abajo

plt.arrow(0.71, 0.01, 0.0, 0.1, color= 'blue', head_width= 0.02)  
plt.arrow(0.84, 0.2, 0.0, 0.1, color= 'blue', head_width= 0.02)    
plt.arrow(0.97, 0.4, 0.0, 0.1, color= 'blue', head_width= 0.02) 

#Detalles del grafico 

plt.title('Hormigas activas en función del parámetro de control', fontsize= 10)
plt.xlabel(r'$\rho$', fontsize= 9)
plt.ylabel('Nivel de actividad', fontsize= 10)


#%%
# Grafico del potencial vs x. 

x= np.linspace(-0.01, 0.6 ,100)

def phi(x,rho, gamma):
    return 0.5*x**3/3- (0.5*rho- gamma)*x**2/2

plt.title('Potencial ')
plt.xlabel('Hormigas activas ')
plt.ylabel(r'$\phi_\rho (x)$')


plt.grid(False)
for rho in [0.3, 0.55, 0.7] : #np.linspace(0,1,10) : 
    plt.plot(x,phi(x,rho, 0.2), label=  f'rho={rho: .1f}')
    
plt.scatter(0,0, s= 100)
plt.scatter(0.3, phi(0.3, 0.7, 0.2), s=100)

plt.legend()
plt.ylim(-0.003, 0.003)


#%%

#Aquí quiero ver qué puntos son estables. Esto debería ser el espacio de fases, de acuerdo a Strogatz 

x=np.linspace(0,1,100)

for rho in np.arange(0,1,0.2): 
    
    plt.plot(x,f(x,tiempo, rho), label=f'rho={rho: .1f}')

    plt.scatter(0, f(0,tiempo, rho ),  color= 'red')
    plt.scatter( gamma/alpha, f(gamma/alpha, tiempo, rho), color= 'red')
    plt.legend()

plt.hlines(0,0,1)
plt.grid(False)
plt.title('Espacio de fases')
plt.ylabel(r'$f(x)= \alpha x (\rho -x)- \gamma x$')
plt.xlabel(r'$x$')

#%% Discusion de los parámetros 

def g(x,gamma, rho, alpha): 
    return alpha* x* (rho- x)- gamma*x 

for gamma in np.arange(0,1,0.2): 
    
    plt.plot(x,g(x,gamma, 1, 1), label=f'gamma={gamma$: .1f}')
    plt.legend()
    
plt.title(r'Espacio de fases para $\gamma$ variable')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.grid(False)
   

#%% 

for alpha in np.arange(0,1,0.2): 
    
    plt.plot(x,g(x,1, 1, alpha), label=f'alpha={alpha: .1f}')
    plt.legend()
    
plt.title(r'Espacio de fases para $\alpha$ variable')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.grid(False)
   

