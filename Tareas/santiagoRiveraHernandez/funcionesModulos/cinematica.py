# Este código... Hace varias cosas, a ver primero leo
# Debo básicamente hacer un código que me haga cálculos cinemáticos en una dirección y luego utilice esos cálculo para calcular parábolas
# Entonces empecemos, ya estudié todos los temas que necesitaba y creo que estoy preparado para hacerlo aunque se vea complicado

# los datos que debo ingresar no son nada nuevo, son los datos de la fórmula de MRUA de posición en 1d
import numpy as np
def pos(r0, v0, a, t):
    # Lo de que "el programa debe aceptar t que sean arrays" me asustó al principio
    # La razón de pedir eso, es que el usuario pueda meter un array y el programa funcione
    # Me preocupa entonces ¿y si el usuario no sabe meter arrays y solo sabe sobre física mecánica, pero quiere usar mi función?
    # Entonces es más fácil, que cualquier cosa que introduzca el usuario, se convierta en un array dentro de la función
    t = np.asarray(t)
    # y listo
    r = r0 + v0*t + (1/2)*(a*t**2)
    return r
def vel(v0, a, t):
    t = np.asarray(t)
    v = v0 + a*t
    return v
# En la siguiente función, el profe definió y0=0.0, pero eso sería incorrecto si queremos que el usuario introduzca la altura inicial
# El punto de eso es que la fórmula, como viene de y = y0 + vt + (1/2)*at^2
# Al despejar t de la fórmula, queda con 2 * g * (y0-y), pero como y = 0 (no y0, y0 es y0, el que es 0 es y), entonces queda solo y0
# Esa notación parece un poco confusa, por lo que si vuelvo a hacer un código así, probablemente yo prefiera usar yi antes que y0
def tVueloParab(v0, theta, y0, g=9.8):
    # Para esta función se debe ingresar el ángulo en grados, pero como no tengo manera de confirmar que esto sea así
    # Solo me queda confiar en que el usuario lo hará de esa manera, cuando use la función, importándola a otro programa desde este archivo
    theta = theta * np.pi / 180
    tVuelo = ( v0*np.sin(theta) + ( (v0*np.sin(theta))**2 + (2 * g * y0))**(0.5) ) / (g)
    return tVuelo
def alcanceMax(v0, theta, x0, y0):
    alfa = theta * np.pi/180
    # Tuve que usar "ángulos diferentes" (solo cambié el nombre) para cada función, porque al hacer el mismo theta la función me daba valores que no eran
    tVuelo = tVueloParab(v0, theta, y0)
    R = x0 + (v0*np.cos(alfa))*tVuelo
    return R

if __name__ == "__main__":
    a = input("¿Qué quiere hacer, posición en 1d (r1d), velocidad en 1d (v1d), tiempo de vuelo parabólico (tvp) o alcance máximo horizontal (amh): ")
    if a == "r1d":
        # r0, v0, a, t
        r0 = float(input("Introduzca la posición inicial: "))
        v0 = float(input("Introduzca la velocidad inicial: "))
        a = float(input("Introduzca la aceleración: "))
        tiempo = input("Introduzca uno o varios tiempos separados por comas sin espacios [1,2,3,4,...,n]: ")
        if "," in tiempo:
            t = np.array([float(n) for n in tiempo.split(",")])
        else:
            t = float(tiempo)
        print(pos(r0,v0,a,t))
    elif a == "v1d":
        # v0, a, t
        v0 = float(input("Introduzca la velocidad inicial: "))
        a = float(input("Introduzca la aceleración: "))
        tiempo = input("Introduzca uno o varios tiempos separados por comas sin espacios [1,2,3,4,...,n]: ")
        if "," in tiempo:
            t = np.array([float(n) for n in tiempo.split(",")])
        else:
            t = float(tiempo)
        print(vel(v0,a,t))
    elif a == "tvp":
        # v0, theta, y0, g=9.8
        v0 = float(input("Introduzca la velocidad inicial: "))
        theta = float(input("Introduzca el ángulo de tiro en grados: "))
        y0 = float(input("Introduzca la altura inicial de tiro: "))
        print(tVueloParab(v0,theta,y0))
    elif a == "amh":
        # v0, theta, x0, y0
        v0 = float(input("Introduzca la velocidad inicial: "))
        theta = float(input("Introduzca el ángulo de tiro en grados: "))
        x0 = float(input("Introduzca la distancia horizontal inicial: "))
        y0 = float(input("Introduzca la altura inicial de tiro: "))
        print(alcanceMax(v0, theta, x0, y0))
    else:
        print("ingrese una de las cuatro opciones de cálculo que se le sugirieron")