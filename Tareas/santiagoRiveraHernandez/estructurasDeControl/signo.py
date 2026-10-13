print("Este programa se encarga de revisar si un número que ingreses es negativo, positivo o cero\n")
a = float(input("Ingrese el número: "))
if a > 0:
    print("\nEl número es positivo")
elif a == 0:
    print("\nEl número es cero")
else:
    print("\nEl número es negativo")