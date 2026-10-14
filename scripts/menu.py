""" Programa que ilustra el uso de los condicionales. Pide el radio
y calcula el diampetro, perímetro y área de un círculo"""
from math import pi

radio = float(input('Entrégame el radio de un círculo en metros: '))

print('####################################')
print('Escoge una opción del siguiente menú:')
print('a) Calcular el diámetro del círculo.')
print('b) Calcular el perímetro del círculo.')
print('c) Calcular el área del círculo.')
option= input('Escoge a, b o c y pulsa enter: ')

if option == 'a':  # Cálculo del diámetro.
    diametro = 2 * radio
    print(f'El diámetro es {diametro:.2f} metros')
elif option == 'b':  # Cálculo del perímetro.
    perimetro = 2 * pi * radio
    print(f'El perímetro es {perimetro:.2f} metros')
elif option == 'c':  # Cálculo del área.
    area = pi * radio ** 2
    print(f'El área es {area:.2f} metros cuadrados')
else:
    print(f'Solo hay tres opciones: a, b o c.')