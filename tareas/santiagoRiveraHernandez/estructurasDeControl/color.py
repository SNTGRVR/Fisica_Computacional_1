print("Este programa le dirá el color aproximado que tiene una onda electromagnética en base a la longitud de onda que usted ingrese: ")

longitud = float(input("Ingrese la longitud de onda en nanómetros de su onda: "))

if longitud < 380:
    print("Su onda es más pequeña que el espectro de luz visible")
elif 380 <= longitud < 427:
    print("Su onda es probablemente morada")
elif 427 <= longitud < 476:
    print("Su onda es probablemente azul")
elif 476 <= longitud < 497:
    print("Su onda es probablemente celeste")
elif 497 <= longitud < 570:
    print("Su onda es probablemente verde")
elif 570 <= longitud < 581:
    print("Su onda es probablemente amarilla")
elif 581 <= longitud < 618:
    print("Su onda es probablemente naranja")
elif 618 <= longitud <= 780:
    print("Su onda es probablemente roja")
else:
    print("Su onda es más grande que el espectro de luz visible")