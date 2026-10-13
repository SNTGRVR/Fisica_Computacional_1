# pi = 8 * sumatoria desde 0 hasta N de { 1 / ( (4k+1) * (4k+3) ) }
# pi = raíz cuadrada de (6 * sumatoria desde 1 hasta N de { 1 / (k**2) } )

import math
print("Este programa se encarga de calcular pi mediante sumatorias, con el esquema de Leibniz y el de Euler\n")
N = int(input("Para empezar, ingrese el N hasta el que se calcularán las sumatorias: "))

#Una sumatoria se puede hacer fácilmente usando while
#Definamos los contadores y las variables que se suman
kL = 0  #L por Leibniz
kE = 1  #E por Euler
sumaL = 0
sumaE = 0

while kL <= N:
    sumaL = sumaL + 1 / ((4*kL+1)*(4*kL+3))
    #Nota que en la fórmula, la sumatoria depende del contador, por lo que no debo confundir kE con kL
    kL = kL + 1
    #En el código de Gauss, imprimí los números que iba sumando el programa y al final mostraba el resultado,
    #pero siento que si lo hago aquí quedaría muy largo
sumaL = 8 * sumaL

while kE <= N:
    sumaE = sumaE + 1 / (kE**2)
    kE = kE + 1
sumaE = (6*sumaE)**(0.5)

print(f"El resultado de pi mediante el esquema de Leibniz es {sumaL}, y mediante el esquema de Euler es {sumaE}")
print(f"Por otra parte, el valor de pi que nos proporciona la librería math es {math.pi}")