"""
Programa que calcula en tiempo de vuelo de un partícula que es 
lanzada verticalmente hacia arriba desde una altura unicial y_0 y con
rapidedz v_0.

El tiempo calculado se compara con el tiempo exacto para estudiar 
el error de presición de la máquina.
"""
import math 

print('----------------------------------')
y0 = float(input('Entre la altura de lanzamiento en metros\t'))
v0 = float(input('Entre la rapidez con la que lo lanzas en m/s\t'))
N = int(input("Entre el número de puntos para el paso del tiempo\t")) 
g = 9.8 # aceleración gravitacional de la tierra en m/s^2
print('----------------------------------')


#--------- solucion exacta ------------
T = (v0 + math.sqrt( v0**2 + 2*g*y0) )/g
#------------------------

t_i = 0.0 # tiempo inicial
t_f = 10. #tiempo final
dt = (t_f - t_i) / (N -1)

t = [] #Lista vacía para el tiempo
y = []  #lista vacía para la altura

#con el for construimos los valores de la altura para cada tiempo
for i in range(N):
    ti = t_i + i * dt #voy incrementando el tiempo
    yi = y0 + v0 * ti - 1/2. * g * ti**2
    t.append(ti)
    y.append(yi)

# con el while buscamos que esa altura siempre sea positiva. 
k = 0
while k < len(y) and y[k]>=0:
    k = k +1

t_num=t[k]

# calculo de errores

err_abs = abs(t_num - T)
err_rel = (err_abs / T) * 100    

print(f"El tiempo que queda la bola en el aire: {t_num:.4f} segundos")
print(f"El tiempo exacto en el que cae la bola es : {T:.4f} segundos")
print("\n--- ANÁLISIS DE ERROR Y PRECISIÓN ---")
print(f"Paso de discretización (dt)   : {dt:.6f} s")
print(f"Error absoluto (|t_num - T|)  : {err_abs:.6f} s")
print(f"Error relativo (%)            : {err_rel:.4f} %")
print(f"La altura para ese tiempo es: {y[k]:.4e} metros")


