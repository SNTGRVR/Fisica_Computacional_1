import math
import numpy as np
print("Este programa se encarga de simular un oscilador armónico simple: ")

def oscilador(A, m, k, phi0, t_max, num_puntos):
    #Calcule la frecuencia angular
    w = math.sqrt(k/m)
    
    #Construya un vector de tiempo de 0 a t_max
    tiempo = np.linspace(0, t_max, num_puntos)
    
    #Evalúe de forma vectorizada con numpy la posición y la velocidad
    
    def posicion(A, w, t, phi0):
        x = A * math.sin(w * t + phi0)
        return x
    xV = np.vectorize(posicion)
    xT = xV(tiempo)

    def velocidad(A, w, t, phi0):
        v = A * w * math.cos(w * t + phi0)
        return v
    vV = np.vectorize(velocidad)
    vT = vV(tiempo)
    return tiempo, xT, vT

def energia_cinetica(v, m):
    Ek = 1/2 * m* (v**2)
    return Ek


def energia_potencial(x, k):
    Ep = 1/2 * k * (x**2)
    return Ep

def energia_total(m, k, x, v):
    E = (1/2) * (m * (v**2) + k * (x**2))
    return E
