print("Esta es una versión del programa 'piscina.py', pero solo usando if-else (no elif)\n")
print("---------------------------------------------------------------------------------\n")
print("Dime la temperatura del agua en celcius, para ver si puedes entrar: ")
t = float(input())
if t > 20 and t <= 30:
    print("No está tan fría, puedes entrar")
else:
    if t >= 15 and t <= 20:
        print("Esta un poco fría, mira a ver")
    else:
        print("Ni se te ocurra meterte a la piscina")