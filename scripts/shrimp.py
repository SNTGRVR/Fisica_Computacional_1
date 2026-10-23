import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# carga de puntos
puntos_x, puntos_y = np.loadtxt("puntos_silueta.txt", unpack=True)
n_puntos = len(puntos_x)

# creación del parámetro t
# t va desde 0 hasta N-1, representando el recorrido a lo largo de la silueta.
t = np.arange(n_puntos)

# interpolación con Splines Cúbicos paramétricos 
# calculamos un spline independiente para las coordenadas X e Y basándonos en t.
X = CubicSpline(t, puntos_x, bc_type='periodic') # 'periodic' asegura transiciones suaves si es cerrado
Y = CubicSpline(t, puntos_y, bc_type='periodic')

# 4. Evaluación en un grid mucho más fino para suavizar el contorno
t_fino = np.linspace(0, n_puntos - 1, 1000)
x_interp = X(t_fino)
y_interp = Y(t_fino)

# plot
plt.figure(figsize=(10, 7))

# Dibujar la silueta continua interpolada
plt.plot(x_interp, y_interp, 'b-', linewidth=2.5, label='Silueta interpolada (Spline Cúbico)')

# Dibujar los puntos del archivo
plt.scatter(puntos_x, puntos_y, color='red', zorder=5, label=f'Puntos del archivo ({n_puntos} puntos)')

plt.title('CAMARÓN', fontsize=14, fontweight='bold')
plt.xlabel('Coordenada X', fontsize=12)
plt.ylabel('Coordenada Y', fontsize=12)
plt.axis('equal') # Importante para que no se deforme la silueta
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left')

plt.show()