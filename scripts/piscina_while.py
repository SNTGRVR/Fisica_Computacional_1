""" Programa que ilustra el uso del while"""
T = float(input("¿Cómo está temperatura del agua?\n Entrégame el valor en Celsius\n"))

while T<= 15 or T>= 27:
    print('No se meta a la piscina')
    break
if 15 < T < 27:
    print('Te puedes meter a la piscina')   