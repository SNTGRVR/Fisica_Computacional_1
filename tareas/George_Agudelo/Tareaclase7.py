numero = int(input("Ingresa un número entero (-128 a 127): "))

if -128 <= numero <= 127:
    binario_8bits = format(numero & 0xFF, '08b')
    print(f"El número {numero} en 8 bits es: {binario_8bits}")
else:
    print("El número está fuera del rango permitido para 8 bits con signo.")