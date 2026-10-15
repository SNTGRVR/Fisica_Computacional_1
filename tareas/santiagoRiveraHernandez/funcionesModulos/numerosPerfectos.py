# Este código te dirá si un número es perfecto o no
# Un número es perfecto si el número es igual a la suma de todos sus divisores menos él mismo
# Ej: 6 = 1 + 2 + 3.            Los divisores de 6 son justamente (1, 2, 3)
# Son divisores porque la división de 6 por estos números es exacta
# Se me ocurre una manera muy sencilla de hacer esta función con un for y la operación %
def perfecto(N):
    if N <= 0:
        print("los números deben ser positivos")
        return None
    divisores = []
    P = 0
    for i in range(1, N):
        if N % i == 0:
            divisores.append(i)
            P = P + i
    if P == N:
        print("El número es perfecto")
        print(f" {' + '.join(map(str, divisores))} es igual a {N} ")
    else:
        print("El número no es perfecto")
        print(f" {' + '.join(map(str, divisores))} es distinto de {N} ")

if __name__ == "__main__":
    n = int(input("Ingrese un número natural cualquiera, el programa le dirá si el número es perfecto o no: "))
    perfecto(n)