import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

datos = np.loadtxt('puntos_silueta.txt')    #Puse el txt en el mismo directorio para no tener que escribir toda su dirección

x = datos[:, 0] #Los dos puntos (:) le dice que tome todas las filas
y = datos[:, 1] #Los números (0 y 1) le dice qué columna tomar
#Esto es así porque en Python se empieza a contar desde 0 y no 1

N = len(x) - 1          #Como empieza contando desde 0, ponemos -1 para que nos de el número de puntos reales
#Creo que esto funciona porque x mide lo mismo que y
t = np.arange(N + 1)    #Arreglo de 0 a N, se pone +1 también por la forma en que lo cuenta

interX = sp.interpolate.CubicSpline(t, x, bc_type='periodic')   #Usamos la función recomendada para interpolar y le decimos que se repita periódicamente
interY = sp.interpolate.CubicSpline(t, y, bc_type='periodic')   #Lo mismo pero con y

mallaT = np.linspace(0, N, 1000)    #Creamos la malla de 1000 puntos para evaluar la interpolación, desde 0 hasta N
#Como N es menor a 1000, básicamente le decimos que genere también los puntos intermedios
#Además, la función los deja espaciados uniformemente, lo cual es bueno para que la curva se vea suave

evalX = interX(mallaT)  #Aplicamos la función en la malla y creamos otra variable por si acaso
evalY = interY(mallaT)  #Lo mismo pero con y

#Ploteamos todo
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='purple', label='Puntos de la silueta', s=20)
plt.plot(evalX, evalY, color='yellow', label='Interpolación cúbica')
plt.grid(True)
plt.xlabel('X', size = 30)
plt.ylabel('Y', size = 30)
plt.title('Interpolación Cúbica de la Silueta')
plt.legend()
plt.axis('equal')
plt.show()