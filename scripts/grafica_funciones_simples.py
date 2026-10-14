""" Uso básico de matplotlib para graficar funciones simples"""
import matplotlib.pyplot as plt # cargamos la librería 
import numpy as np #cargamos numpy

#-----------
# figfura 1
#----------

teta = np.linspace(-2*np.pi, 2*np.pi, 100) # crea linspace
sint = np.sin(teta) # calcula el seno
cost = np.cos(teta) # calcula el coseno

plt.figure(1)
plt.plot(teta,sint,'r-',label= r'$\sin(\theta)$')
plt.plot(teta,cost,'b--',label= r'$\cos(\theta)$')
plt.xlabel(r'$\theta$', size=15)
plt.legend(loc='upper right')
plt.xlim(-2*np.pi, 2*np.pi)
plt.ylim(-1,1)
plt.savefig('senocoseno.pdf', bbox_inches='tight')

#----------
# figura 2
#-----------

x = np.linspace(0,100, 100)
logx = np.log(x) # note el error al calular el log0
sqrtx = np.sqrt(x)

plt.figure(2)
plt.plot(x,logx,'r-.',lw = '5', label= r'$\ln(x)$')
plt.plot(x,sqrtx,'b-',lw ='3.',label= r'$\sqrt{x}$')
plt.xlabel(r'$x$', size=15)
plt.legend(loc='upper left')
plt.xlim(0, 100)
plt.savefig('log10sqrt.pdf', bbox_inches='tight')


plt.show()