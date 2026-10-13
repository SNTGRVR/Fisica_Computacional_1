import math
print("Este programa se encarga de darle la altura de la superficie de la tierra, " \
"a la que debe soltar un satélite, para que este orbite la tierra cada T segundos")

G = 6.67e-11   #Constante de gravitación universal
M = 5.97e24     #Masa de la tierra en kilogramos
R = 6371000     #Radio de la tierra en metros

minutos = float(input("Ingrese el tiempo que quiere que dure la órbita del satélite en minutos: "))
segundos = minutos * 60

# h = (GMT^2 / 4pi^2)^(1/3) - R
altura = ( G*M*(segundos**2) / (4*math.pi**2) )**(1/3.) - R
print(f"La altura a la que debe lanzar el satélite es de {altura} metros")
kilometers = altura / 1000
print(f"\nLa altura en kilómetros sería {kilometers}")