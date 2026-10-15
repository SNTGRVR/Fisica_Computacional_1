import math

print("Este programa se encarga de convertir" \
" posiciones en coordenadas polares a coordenadas cartesianas")

distancia = float(input("Ingrese la distancia r a la que está el punto: "))
grados = float(input("Ingrese el ángulo al que se encuentra el punto dado, en grados: "))
radianes = grados * (math.pi / 180)

print(f"Como en cálculo se acostumbra a usar radianes," \
" se han convertido los grados que usted ingresó a radianes," \
" por ende, los grados que usted ingresó se han registrado como:\n")
print(radianes)

x = distancia * math.cos(radianes)
y = distancia * math.sin(radianes)

print("\nCon esto hecho, la posición que usted ingresó en coordenadas polares," \
" quedan así en coordenadas cartesianas:\n")

print(f"{x}, {y}")