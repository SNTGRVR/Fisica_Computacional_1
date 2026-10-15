import sys
print("Este programa hará el cálculo de las raíces de una ecuación cuadrática\n"
      "Ingrese las constantes a, b y c correspondientes:\n")

a = float(input("Ingrese a: "))
if a == 0:
    print("Si a es cero, la ecuación no es cuadrática")
    sys.exit()
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

# Para la ecuación cuadrática ax^2 + bx + c = 0, las posibles soluciones de x se pueden calcular con la fórmula del bachiller
# x = (-b +- sqrt(b^2 - (4ac))) / 2a

determinante = b**2 - (4*a*c)

if determinante >= 0:
    firstRoot = (-b + (determinante)**0.5) / (2*a)
    secondRoot = (-b - (determinante)**0.5) / (2*a)
    print("Las raíces de la ecuación cuadrática son las siguientes: ")
    print(firstRoot, secondRoot)

else:
    print("La ecuación no tiene soluciones reales")