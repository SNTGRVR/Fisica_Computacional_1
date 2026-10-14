import numpy as np
import matplotlib.pyplot as plt

print('----------------------------------')
y0 = float(input('Entre la altura de lanzamiento en metros\t'))
v0 = float(input('Entre la rapidez con la que lo lanzas en m/s\t'))
N = int(input("Entre el número de puntos para el paso del tiempo\t")) 
g = 9.8 # aceleración gravitacional de la tierra en m/s^2
print('----------------------------------')


#--------- solucion exacta ------------
T = (v0 + np.sqrt( v0**2 + 2*g*y0) )/g
#------------------------

t_i = 0.0 # tiempo inicial
t_f = 10. #tiempo final
t = np.linspace(t_i, t_f, N) # arreglo con los tiempos

# arreglo vectorizado con las alturas 
# con esto nos ahorramos un for
y = y0 + v0 * t - 1/2. * g * t**2 

# con el while buscamos que esa altura siempre sea positiva. 
i = 0
while y[i] >=0:
    i = i +1

t_num=t[i]

# calculo de errores

err_abs = abs(t_num - T)
err_rel = (err_abs / T) * 100    

print(f"El tiempo que queda la bola en el aire: {t_num:.4f} segundos")
print(f"El tiempo exacto en el que cae la bola es : {T:.4f} segundos")
print("\n--- ANÁLISIS DE ERROR Y PRECISIÓN ---")
print(f"Error absoluto (|t_num - T|)  : {err_abs:.6f} s")
print(f"Error relativo (%)            : {err_rel:.4f} %")
print(f"La altura para ese tiempo es: {y[i]:.4e} metros")

# ---------------------------------------------------------
# INTRODUCCIÓN A MATPLOTLIB (Solo 4 comandos básicos)
# ---------------------------------------------------------
plt.plot(t, y, label='Trayectoria y(t)')            # Curva continua
plt.axhline(0, color='black', linestyle='--')       # Línea del suelo (y = 0)
plt.plot(t[i], y[i], 'ro', label=f'Impacto con el suelo (i={i}, t(i)={t[i]:.4f} s)') # Punto numérico detectado

plt.xlabel('Tiempo [s]')
plt.ylabel('Altura [m]')
plt.title(f'Movimiento Parabólico. El tiempo exacto es {T:.4f} s')
plt.grid(True)
plt.legend()
plt.ylim(-0.5,2)
plt.xlim(0,1)
plt.savefig('parabolico.pdf', bbox_inches='tight') #guardar
plt.show()  # Despliega la ventana con la gráfica