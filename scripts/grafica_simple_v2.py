""" Uso básico de matplotlib"""
import matplotlib.pyplot as plt # cargamos la librería

#construimos listas
x = [0., 0.5, 1., 1.5, 2., 2.5, 3] 
t = [1., 1., 2., 3., 5., 8., 13.]

plt.plot(x,t,'r.',ms='15')
plt.xlabel(r'$x\,[\mathrm{m}]$',size=15)
plt.ylabel(r'$t\,[\mathrm{s}]$', size=15)

plt.savefig('grafica_simple_v2.pdf', bbox_inches='tight')
plt.show()

