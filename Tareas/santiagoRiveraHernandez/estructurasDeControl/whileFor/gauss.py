print("Este programa calculará una suma de gauss hasta n: ")

n = int(input("Ingrese el número n hasta el que quiere calcular la suma: "))
contador = 1
suma = 0

print(f"{suma} +")
while contador <= n:
    print(f"{contador} +")
    suma = suma + contador
    contador = contador + 1

print(f"El resultado de la suma es {suma}")
fórmula = n*(n+1)/2
print(f"La fórmula es {n}*{n+1}/{2}, que da como resultado {fórmula}")