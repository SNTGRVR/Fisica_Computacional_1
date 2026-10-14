import math 

N = int(input("Hola, dame el número de términos para la suma. Debe ser entero:\n"))

sumaL = 0#primer valor del esquema Leibniz
sumaE = 0 #primer valor del esquema Euler

#Esquema de Leibniz
kl = 0 # contador inicia 1n 0
while kl < N:
    terminoL = 8/((4*kl + 1)*(4*kl + 3))
    sumaL = sumaL + terminoL
    kl = kl + 1

#Esquema de Euler
ke = 1 # contador inica en 1
while ke <= N:
    terminoE = 1/ke**2
    sumaE = sumaE + terminoE
    ke = ke + 1
print("-----------------------------------------------------")
print(f"En el esquema de Leibiniz, π ~ {sumaL:.5f}")
print(f"En el esquema de Euler,  π ~ {math.sqrt(6*sumaE):.5f}")
print(f"El que trae la librería math,  π ~ {math.pi:.5f}")
print("-----------------------------------------------------")

