""" Programa que ilustra el uso del while, break y continue"""
while True: # el while recibe un booleano. Hasta que no se  pueda meter a la pisina. No para
    T = float(input("¿Cómo está la temperatura del agua?\nEntrégame el valor en Celsius:\n"))
    
    if T <= 15 or T >= 27:
        print('No se meta a la piscina.\n')
        continue  # Salta el mensaje final y vuelve al inicio del while a pedir T de nuevo
    
    # Esta línea solo se alcanza si la condición del 'if' fue falsa
    print('Te puedes meter a la piscina.')
    break  # Rompe el bucle porque ya obtuvimos un valor válido