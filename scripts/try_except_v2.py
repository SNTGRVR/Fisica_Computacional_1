"""Uso básico del try-except"""
try:
    a = float(input("Entre a\n"))
    b = float(input("Entre b\n"))

    solution = -b / a

except ZeroDivisionError: # analiza si a =0 
    print("Error: El coeficiente 'a' debe ser diferente de cero.")

except ValueError: # analiza si alguna variable que entra no es un número
    print("Error: Debe ingresar un valor numérico válido.")

else:
    # Este bloque solo se ejecuta si la división en try fue exitosa
    print("Las variables ingresadas son correctas\n")
    print(f"La solución es x = {solution:.3f}")