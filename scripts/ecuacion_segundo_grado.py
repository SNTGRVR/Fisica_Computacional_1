"""Uso básico del try-except"""
import math

try:
    a = float(input("Entre a\n"))
    b = float(input("Entre b\n"))
    c = float(input("Entre c\n"))

    d = b**2 - 4 * a * c #discriminante

    x1 = (-b - math.sqrt(d))/(2 * a)
    x2 = (-b + math.sqrt(d))/(2 * a)

except ZeroDivisionError: # analiza si a =0 
    print("Error: El coeficiente 'a' debe ser diferente de cero.")

except ValueError: # analiza si alguna variable que entra no es un número
    print("Error: Puede que no haya ingresado un valor numérico\n o que no haya solucióon en los reales.")

else:
    # Este bloque solo se ejecuta si la división en try fue exitosa
    print("Las variables ingresadas son correctas\n")
    print(f"Lad soluciones son  x_1 = {x1:.3f} y x_2 = {x2:.3f} ")