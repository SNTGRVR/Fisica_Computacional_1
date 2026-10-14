""" Este es un ejemplo del uso de funciones """

def factorial(n):
    ''' Calcula el factorial de un número entero'''
    f = 1
    for i in range(1,n+1):
        f = i * f
    return f

### acá comenzamos el programa

a = int(input("ingrese el número entero del que quiere conocer el factrorial\n"))

if a>=0:
    elfatorial = factorial(a)
    print(f"El factorial del número que entraste es: {elfatorial} ")
else:
    print("No es la función Gamma, el número debe ser entero mayor o igual a cero.")




