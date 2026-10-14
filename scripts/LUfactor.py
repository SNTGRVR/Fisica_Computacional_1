""" Aquí se muestran algunas funciones básicas para trabajar con matrices"""

import numpy as np
import scipy as sp

# definición de la matrix
A = np.array([[2,1,4,1], [3,4,-1,-1], [1,-4,1,5], [2,-2,1,3]], dtype=float)

# definición del vector
v = np.array([4,-3,9,7], dtype=float)

# ==== Descomposición LU=====
# P es la matriz de permutación, L es triangular inferior y U triangular superior
P, L, U = sp.linalg.lu(A)

print("=== DESCOMPOSICIÓN LU (P A = L U) ===")
print(f"Matriz P (Permutación):\n{P}\n")
print(f"Matriz L (Triangular Inferior con 1s en la diagonal):\n{L}\n")
print(f"Matriz U (Triangular Superior):\n{U}\n")

# Verificación de la descomposición P @ L @ U == A
print(f"Verificación P @ L @ U == A:")
print(f"{P @ L @ U}\n")

# Resolución del sistema Ax = v usando LU (L y = P^T v, luego U x = y)
y_lu = sp.linalg.solve_triangular(L, P.T @ v, lower=True)
x_lu = sp.linalg.solve_triangular(U, y_lu, lower=False)

residuo1 = (A @ x_lu) -v
print(f"Solución x usando Descomposición LU:\nx = {x_lu}\n")
print(f"con residuo:\n {residuo1}\n")

if not np.isclose(np.linalg.det(A),0): 
    # solución del sistema usando np.linag.solve 
    y = np.linalg.solve(A,v)
    residuo2 = (A @ y) - v
    print(f"Por otro lado, podemos encontrar directamente la solución al sistema utilizando np.linalg.solve\n x = {y}")
    print(f"Con residuo = {residuo2}")

else:
    print("La matriz A tiene determinante nulo, por lo tanto no es invertible")

