""" Aquí se muestran algunas funciones básicas para trabajar con matrices"""

import numpy as np

# definición de la matrix
A = np.array([[2,1,4,1], [3,4,-1,-1], [1,-4,1,5], [2,-2,1,3]], dtype=float)

# definición del vector
v = np.array([4,-3,9,7], dtype=float)

# ==== propiedades de la matriz=====
detA = np.linalg.det(A) # determinante
rango = np.linalg.matrix_rank(A) #rango
transpuestaA = np.transpose(A) # transpuesta también pued usar A.T
trazaA = np.trace(A) #traza

print("=== PROPIEDADES DE LA MATRIZ A ===")
print(f"Rango: {rango}")
print(f"Traza: {trazaA}")
print(f"Determinante: {detA:.2f}")
print(f"Transpuesta:\n{transpuestaA}\n")

if not np.isclose(detA,0): 
    print(f"El determinante de A es \n det A={detA: .2f}, diferente de cero")

    # método de la inversa
    invA = np.linalg.inv(A)
    x = invA @ v # note el uso del operador @ antes se usaba np.dot(invA,v)
    residuo1 = (A @ x) - v

    print(f"\nSu inversa es \n A^-1 = {invA}")
    print(f"\nLa solución del sistema usando la inversa es \n x = {x}")
    print(f"\nCon residuo = {residuo1}")

    # solución del sistema usando np.linag.solve 
    y = np.linalg.solve(A,v)
    residuo2 = (A @ y) - v
    print(f"\nPor otro lado, podemos encontrar directamente la solución al sistema utilizando np.linalg.solve\n x = {y}")
    print(f"\nCon residuo = {residuo2}")

else:
    print("La matriz A tiene determinante nulo, por lo tanto no es invertible")

