import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
print("1. Raíces de un polinomio")
x = sp.symbols("x")
pX = 2*x**3 - 3*x**2 - 11*x + 6
print(f"El polinomio es: {pX}")
print("las raíces son: ")
print(sp.roots(pX))
print(sp.solve(pX))

print("="*60)

print("2. Descomposición de una función")
fX = (5*x - 2) / (x**2 - x - 6)
print(f"La función es: {fX}")
print("Al descomponerla en fracciones simples: ")
print(sp.apart(fX))

print("="*60)

print("3. Puntos de intersección")
y = sp.symbols("y")
print("Tenemos la ecuación del círculo x^2 + y^2 = 25")
print("Y la ecuación de la recta y - 2x = 1")

reemplazo = x**2 + (2*x+1)**2 - 25
respuesta = sp.solve(reemplazo, x)
print(respuesta)

#Parte matplotlib

"""Necesito las variables independientes del círculo y la recta"""
X = np.linspace(-6, 6, 100)
T = np.linspace(0, 2*np.pi, 100)

"""Ahora necesito definir ambas ecuaciones en base a las variables independientes"""
rec = 1 + 2*X
cirY = 5 * np.sin(T)
cirX = 5 * np.cos(T)

plt. figure(figsize=(6, 6))
plt.plot(cirX, cirY, label="Círculo")
plt.plot(X, rec, label="Recta")

plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)

plt.grid(True)
plt.axis("equal")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Intersección entre círculo y recta")
plt.legend()

plt.show()