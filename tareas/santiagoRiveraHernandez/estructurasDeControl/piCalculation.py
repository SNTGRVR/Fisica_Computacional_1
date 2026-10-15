import math
print("Calcularemos pi, entonces, introduzca N, que es el numero hasta donde se hará el cálculo de pi mediante sumatorias")

N = int(input())
k1 = 0
k2 = 1
suma1 = 0
suma2 = 0

while k1 <= N:
    suma1 = suma1 + (1 / ((4 * k1 + 1) * (4 * k1 + 3)))
    k1 = k1 + 1
suma1 = 8 * suma1
print("el cálculo de pi mediante el esquema de Leibniz es: ")
print(suma1)

while k2 <= N:
    suma2 = suma2 + (1 / k2**2)
    k2 = k2 + 1
suma2 = math.sqrt(6 * suma2)
print("el cálculo de pi mediante el esquema de Euler es: ")
print(suma2)

print("pi es: ")
print(math.pi)
errorSuma1 = abs( (suma1 - math.pi) / suma1 ) * 100
errorSuma2 = abs( (suma2 - math.pi) / suma2 ) * 100
print("El porcentaje de error para el esquema de Leibniz es: ")
print(errorSuma1)
print("El porcentaje de error para el esquema de Euler es: ")
print(errorSuma2)