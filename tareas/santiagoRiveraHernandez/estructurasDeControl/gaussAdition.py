import math
print("Haremos la suma de 1+2+3... hasta el N de su elección, entonces, introduzca N")
N = int(input())
k = 1
suma = 0
while k <= N:
    suma = suma + k
    k = k + 1
print("El resultado de la suma es: ")
print(suma)

print("La fórmula de Gauss para esta sumatoria es N(N+1)/2, de esta manera la suma da: ")
Gauss = (N * (N + 1)) / 2
print(Gauss)