import math
print("Este código se encarga de calcular la variación de la cantidad de una sustancia radioactiva")
#N(t) = N0 * e**(-lambda * t)


N0 = float(input("Introduzca la cantidad inicial de la sustancia: "))
n = N0 * 0.1
X = float(input("Inttroduzca la constante de decaimiento de la sustancia: "))
t = 1
N = N0 #Igualamos ambas variables porque al inicio ambas refieren a la cantidad de la sustancia, pero solo una refiere a como va decayendo

#N = n * e**(-X * t)

while N >= n:
    N = N0 * math.e**(-X * t)
    t = t + 1

print(f"La cantidad final de la sustancia fue {N}")
print(f"Esta cantidad se alcanzó pasados los {t-1} años")