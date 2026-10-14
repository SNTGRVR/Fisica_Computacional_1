""" Aplicamos la transformación biunitaria para diagonalizar una matrix
en matemáticas se conoce como el singular value descomposition (SVD)"""
import numpy as np


# Matriz de masa cuadrada (3 x 3)
M = np.array([[2.0 + 1j,  0.5 - 0.2j, 1.0], [0.1,1.5 + 0.8j, 0.3j], [0.0, 0.2, 0.8 - 0.5j] ])

# Aplicamos SVD (Transformación biunitaria)
# U y V son unitarias (en partículas son V_L y V_R) Md es S, la diagonal
VL, Md, VRh = np.linalg.svd(M)

# contruimos el VR porque la rutina devuelve el hermítico
VR = VRh.conj().T

# Verificamos la diagonalización V_L^\dagger @ M @ V_R
M_diag = VL.conj().T @ M @ VR

print("======= matrix M cuadrada 3x3 ========")
print("Masas físicas (Valores singulares S con np.linalg.svd(M)):")
print(np.round(Md, 4))

print("\nMatriz diagonalizada V_L^H @ M @ V_R:")
print(np.round(M_diag, 4))

# Matriz de masa  no cuadrada cuadrada (3 x 4)
N = np.array([[2.0 + 1j,  0.5 - 0.2j, 0.0, 1. -1j], [0.1,1.5 + 0.8j, 0.3j, 1. -2j ], [0.0, 0.2, 0.8 - 0.5j, 1. +3j] ])
# Aplicamos SVD (Transformación biunitaria)
# U y V son unitarias (en partículas son V_L y V_R) Md es S, la diagonal
VNL, MNd, VNRh = np.linalg.svd(N)

# contruimos el VR porque la rutina devuelve el hermítico
VNR = VNRh.conj().T

# Verificamos la diagonalización V_L^\dagger @ M @ V_R
MN_diag = VNL.conj().T @ N @ VNR

print("\n======= matrix N no cuadrada 3x4 ========")
print(f"Dimensiones de N:   {N.shape}")
print(f"Dimensiones de VNL: {VNL.shape}  | VNR: {VNR.shape}")

print("Masas físicas (Valores singulares S con np.linalg.svd(MN):")
print(np.round(MNd, 4))

print("\nMatriz diagonalizada VN_L^H @ N @ VN_R:")
print(np.round(MN_diag, 4))
print(f"El rango de N es: {np.linalg.matrix_rank(N)} que equivale a las masas físicas")