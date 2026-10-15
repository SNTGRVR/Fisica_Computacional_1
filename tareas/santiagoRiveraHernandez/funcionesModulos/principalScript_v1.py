# Aquí vamos a probar cinematica.py
import numpy as np
import cinematica as cine
print("Un cañón situado a y0=35m dispara proyectiles a v0 = 40m/s, varíe el ángulo de lanzamiento theta desde 10° hasta 80° en pasos de 1°")
# Okey... ¿Un array o un for, cuál sería mejor?
# Por ahora ese problema en específico no requiere de usar ninguna de las funciones de cinematica.py
# Ya no tengo ganas de programar DDDDDDDDDDDD: ahhhhhhhhAHHHHHHH
# AQAAAAAAAAHHHHHHHH, esto es lo que me pasa por hacer las cosas tarde
y0 = 35
print(f"La altura inicial es de {y0}")
v0 = 40
print(f"La velocidad inicial es {v0}")
# No me dice que le pida al usuario el ángulo, sino que lo varíe desde 10° hasta 80°
# Quiero suponer que me pide que lo haga como lista, porque es lo que hemos visto
theta = []
for i in range(10,81):
    theta.append(i)
print(theta)
# Bueno, eso lo haría, lo imprimo por si acaso

# Lo siguiente es encontrar el ángulo óptimo que maximice el alcance horizontal R y el tiempo de vuelo correspondiente
# Por la forma en que lo dice, probablemente solo necesito que el programa pase por todos los valores de theta hasta que R sea más lo más grande posible
# Aunque... No sé si sea tan sencillo así, pues sería como siempre estar comprobando que R sea mayor al R anterior
# Otra manera sería hacer el cálculo con todos los ángulos y guardar los respectivos R en una lista, que luego muestre cuál es el R más grande de la lista...
# ¿Pero no me lleva al mismo problema?, debe haber una solución más sencilla

# Bueno, por ahora probemos

print("Usando las funciones de su módulo, encuentre numéricamente el ángulo óptimo que maximiza el alcance horizontal R y el tiempo de vuelo correspondiente")
# Lo que entiendo de ese enunciado es que debo hallar R máximo, el ángulo en que hallo ese R máximo y decir el tiempo que tiene en ese ángulo
# La otra posibilidad es que deba hallar R máximo y su ángulo, y aparte T máximo y su ángulo
# Ambas son sencillas de programar, para la primera opción simplemente debo llamar tVueloParab por fuera del for, usando el ángulo en el que R es máximo como variable
# La segunda opción es simplemente llamar tVueloParab dentro del for, y por fuera usar max para hallar el T máximo y luego usar index para hallar el ángulo en el que alcanza ese T máximo
x0 = float(input("Ingrese la distancia horizontal inicial: "))
r = []
for i in range(10,81):
    # angulo = i
    # v0, theta, x0, y0
    r.append(cine.alcanceMax(v0,i,x0,y0))
# Python tiene dos funciones maravillosas llamadas max e index, una me da el número más grande de una lista de números, la otra me da la posición en la que está un valor cualquiera que escoja de una lista cualquiera que escoja
R = max(r)
anguloR = r.index(R) + 10
# v0, theta, y0, g=9.8
T = cine.tVueloParab(v0, anguloR, y0)
print(f"La mayor distancia horizontal recorrida es {R}, se obtiene cuando el ángulo es {anguloR}")
print(f"El tiempo que se mantiene en el aire cuando es lanzado en ese ángulo es {T}")
# Al parecer el siguiente paso era imprimir los resultados, pero es tan natural hacerlo que lo escribí sin pensar
# Me falta hacer los gráficos, probablemente es con Matplotlib pero no lo he estudiado, esta será la primera versión del código
# Cuando estudie matplotlib, haré una segunda versión