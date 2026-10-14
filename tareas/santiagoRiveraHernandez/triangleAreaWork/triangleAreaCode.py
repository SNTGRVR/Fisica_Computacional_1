print("Este es un archivo python que te calculará el área de un triángulo en función de la base y altura que introduzcas")
base = float(input("Introduzca el valor de la base del triángulo: "))
if base < 0:
	print("Eres tonto, pero te lo voy a pasar")
altura = float(input("Introduzca el valor de la altura del triángulo: "))
if altura < 0:
	print("Date cuentaa")
area = abs((1/2) * base * altura)
print(f"El área del triángulo es: {area}")
