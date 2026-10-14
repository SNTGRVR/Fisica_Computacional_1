"""En este programa se ilustra el uso de la lectura de datos para graficarlos"""
import numpy as np
import matplotlib.pyplot as plt

datos= np.loadtxt('datosL1.txt')
l = datos[:,0] # la primera columna es la longitud
t = datos[:,1] # la segunda columna es el tiempo
#calculo de la masa gravitacional/ masa inercial
mgmi = 4.0281 * l / (t**2)

# plot
plt.figure(figsize=(8, 6))
plt.plot(t, mgmi, color='red', ls='-', lw=3, label=r'$\boldsymbol{Datos}$')
plt.yscale('log')
plt.ylim(0.1,10)
plt.axhline(1, color='black', ls='--', lw=3, label=r'$\boldsymbol{Esperado}$')
plt.xlabel("tiempo(s)", size=20)
plt.ylabel(r'$\boldsymbol{m_g/m_i}$', size=20)
plt.legend(prop={'size': 15}, loc='upper left', frameon=True)
plt.savefig("mgvsmi.pdf")
plt.show()