def factorial(n):
    '''Esta función muestra todo el cálculo para el factorial de un número entero positivo, debe ingresar el número al que le va a calcular el factorial'''
    f = 1
    for i in range(1, n+1):
        f = f * i
        print(f)
    return f

n = int(input("Escriba el valor de n para sacarle factorial: "))

factorial(n)