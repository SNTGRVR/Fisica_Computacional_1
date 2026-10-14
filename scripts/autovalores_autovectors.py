""" Aquí se muestran las funciones básicas para calcular autovectores y autovalores"""

import numpy as np

# definición de la matrix
M = np.array([[2,1,4,1,7], [3,4,-1,1,0], [1,-4,1,5,2], [2,-2,1,3,6], [-1,-3,2,1,-10] ], dtype=float)

# ==== Autovalores y autovectrores propiedades de la matriz=====
autovalores, autovectores = np.linalg.eig(M)

print("=== AUTOVALORES Y AUTOVECTORES ===")
print(f"Autovalores (λ):\n{autovalores}\n")
print(f"Autovectores (columnas v_i):\n{autovectores}\n")

print("----------------\n")
print("Verificación de la relación A * v = λ * v sin usar enumerate")
print("----------------\n")

for i in range(len(autovalores)):
    lamvi = autovalores[i]
    vi = autovectores[:,i]
    lamv = lamvi * vi
    Mv = M @ vi
    print(f"Autovalor λ_{i} = {lamvi:.4f}")
    print(f"  M @ v_{i}:     {Mv}")
    print(f"  λ_{i} * v_{i}:    {lamv}")
    # Comprobación de igualdad numérica
    print(f" ¿Son iguales? {np.allclose(Mv, lamv)}\n")

print("----------------\n")
print("Verificación de la relación A * v = λ * v usando enumerate")
print("----------------\n")

for i, lam in enumerate(autovalores):
    vi = autovectores[:, i]
    Mv = M @ vi
    lamv = lam * vi
    print(f"Autovalor λ_{i} = {lam:.4f}")
    print(f"  M @ v_{i}:     {Mv}")
    print(f"  λ_{i} * v_{i}:    {lamv}")
    # Comprobación de igualdad numérica
    print(f" ¿Son iguales? {np.allclose(Mv, lamv)}\n")
