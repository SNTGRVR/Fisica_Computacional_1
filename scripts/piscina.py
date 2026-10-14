""" Programa que ilustra el uso de los condicionales"""
T = float(input("¿Cómo está temperatura del agua?\n Entregame el valor en Celsius\n"))
if T > 20 and T < 27:
    print('te puedes meter a la piscina')
elif 15 <= T <= 20:
    print('El agua está medio fría, usted verá')
else:
    print('No se meta a la piscina')