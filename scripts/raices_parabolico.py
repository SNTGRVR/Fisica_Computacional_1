""" En este programa se utiliza la librería scipy 
    para encontrar los ángulos de lanzamiento de un cuerpo para 
    una altura máxima y una distancia horizontal máxima"""

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

def x_max(theta, x0=0., y0 = 0., v0 = 3.5, g = 9.8):
    """ función para encontrar el desplazamiento máximo horizontal. 
    Variables de entrada. theta:  ángulo en metros. y0: altura inicial en metros.
    v0: magnitud de la velocidad inicial en m/s. g: aceleración gravedad en m/s^2"""
    sintheta = np.sin(np.radians(theta))
    costheta = np.cos(np.radians(theta))
    prefactor = ( v0 * costheta )/g
    return x0 + prefactor * (v0 * sintheta + np.sqrt(v0**2 * sintheta**2 + 2*g*y0) )

def y_max(theta, y0 = 0., v0 = 3.5, g = 9.8):
    """ función para encontrar la altura máxima. 
    Variables de entrada. theta:  ángulo en metros. y0: altura inicial en metros.
    v0: magnitud de la velocidad inicial en m/s. g: aceleración gravedad en m/s^2"""
    sintheta = np.sin(np.radians(theta))
    return y0 + 1/(2.*g) * v0**2 * sintheta**2

def f_x(theta, xmaximo, x0, y0, v0, g):
    """Función asociada al alcance horizontal máximo:  xmaximo - x_max(theta,...) = 0"""
    return x_max(theta, x0, y0, v0, g) - xmaximo

def f_y(theta, ymaxima, y0, v0, g):
    """Función asociada a la altura máxima:  ymaximo - y_max(theta,...) = 0"""
    return y_max(theta, y0, v0, g) - ymaxima


if __name__ == "__main__":
    y0 = 1.5      # Altura inicial (m)
    x0 = 0.0      # Posición inicial (m)
    v0 = 35.0     # Velocidad inicial (m/s)
    g = 9.8       # Gravedad (m/s^2)
    xmaximo = 89.0 # Alcance máximo (m)

    angulos = np.linspace(0, 90, 300)
    alcancesx = x_max(angulos, x0, y0, v0, g)

    plt.figure(figsize=(8, 5))
    plt.plot(angulos, alcancesx, label=r'$x_{\mathrm{max}}(\theta)$', color='blue', lw=2)
    plt.axhline(xmaximo, color='red', linestyle='--', label=rf'$x_{{max}} = $ {xmaximo} m')
    plt.title(f'Alcance Horizontal vs Ángulo ($v_0 = {v0}$ m/s, $y_0 = {y0}$ m)', fontsize = 15)
    plt.xlabel(r'$\theta$ (grados)', fontsize = 15)
    plt.ylabel('$x$ (m)',fontsize=15)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend(loc='lower center', fontsize = 15)
    plt.tight_layout()

    try: 
        sol1 = sp.optimize.root_scalar(f_x, args=(xmaximo, x0, y0, v0, g), bracket=[0, 45], method='brentq')
        sol2 = sp.optimize.root_scalar(f_x, args=(xmaximo, x0, y0, v0, g), bracket=[45, 90], method='brentq') 

        res1 = f_x(sol1.root, xmaximo, x0, y0, v0, g)
        res2 = f_x(sol2.root, xmaximo, x0, y0, v0, g)

        print(f"\n--- Ángulos con que se debe lanzar la pelota para un alcance máximo de = {xmaximo} metros---")
        print(f"Ángulo 1  : {sol1.root:.4f}°| Error: {abs(res1):.2e} m  | Iteraciones: {sol1.iterations}")
        print(f"Ángulo 2 : {sol2.root:.4f}° | Error: {abs(res2):.2e} m | Iteraciones: {sol2.iterations}")

    except ValueError:
        # Ocurre un error si no encuentra soluciones 
        alcance_max_posible = np.max(alcancesx)
        print(f"\n[Error] El alcance deseado de {xmaximo} m es físicamente inalcanzable.")
        print(f"El alcance máximo posible con v0={v0} m/s y y0={y0} m es de {alcance_max_posible:.2f} m.")    

    plt.savefig('../Clases/Herramientas_Python/alcance_vs_angulo.pdf', bbox_inches='tight')
    plt.show()               