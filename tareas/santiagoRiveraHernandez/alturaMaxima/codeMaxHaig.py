# Con el pseudocódigo hecho, podemos pasar a hacer el código
g = -9.81
h = float(input("Introduzca la altura que desea alcanzar: "))
hInicial = float(input("Introduzca la altura inicial: "))
vInicial = float(input("Introduzca la velocidad inicial: "))
if vInicial < 0:
    print("No quiero calcular rebotes, tomaré la velocidad que me diste como positiva")
    vInicial = abs(vInicial)
if vInicial**2 < 2*g*(h-hInicial):
    print("El objeto nunca alcanzará la altura deseada")
# Calcular una raíz cuadrada es elevar a la 0.5... Por si no sabías
else:
    # Ya que tomamos la gravedad como negativa por eso de "ir hacia abajo", cambié un poco la fórmula
    tSuma = (-vInicial + ((vInicial**2) - 2*g*(h-hInicial))**0.5) / g
    tResta = (-vInicial - ((vInicial**2) - 2*g*(h-hInicial))**0.5) / g
    print(tSuma, tResta)
    print("Decide bajo tu criterio si ambos tiempos tienen sentido físico o no lo tienen")
