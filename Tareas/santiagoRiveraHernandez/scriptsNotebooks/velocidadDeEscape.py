import sys
print("Este código se encarga de calcular la velocidad de escape de cualquier planeta del sistema solar\n")

#velocidad de escape = raíz cuadrada de ( (2 * G * M) / R )

G = 6.674e-11 # Constante gravitatoria universal de Newton
planeta = str(input("Ingrese el planeta del que quiere calcular la velocidad de escape (escriba todo en minúsculas): "))
# Por ahora no conozco una manera de evitarme hacer un montón de elif, cuando lo sepa haré una variación a este código
if planeta == "mercurio":
    M = 3.30e23
    R = 2440000
    print(f"La masa de {planeta} es de {M} kilogramos, su radio es de {R} metros")
elif planeta == "venus":
    M = 4.87e24
    R = 6052000
    print(f"La masa de {planeta} es de {M} kilogramos, su radio es de {R} metros")
elif planeta == "tierra":
    M = 5.972e24
    R = 6371000
    print(f"La masa de {planeta} es de {M} kilogramos, su radio es de {R} metros")
elif planeta == "marte":
    M = 6.42e23
    R = 3390000
    print(f"La masa de {planeta} es de {M} kilogramos, su radio es de {R} metros")
elif planeta == "urano":
    M = 8.68e25
    R = 25362000
    print(f"La masa de {planeta} es de {M} kilogramos, su radio es de {R} metros")
elif planeta == "neptuno":
    M = 1.02e28
    R = 24622000
    print(f"La masa de {planeta} es de {M} kilogramos, su radio es de {R} metros")
elif planeta == "saturno":
    M = 5.68e28
    R = 58232000
    print(f"La masa de {planeta} es de {M} kilogramos, su radio es de {R} metros")
elif planeta == "júpiter":
    M = 1.90e27
    R = 69911000
    print(f"La masa de {planeta} es de {M} kilogramos, su radio es de {R} metros")
elif planeta == "plutón":
    print("Plutón no es un planeta")
    sys.exit("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
else:
    print("Revisa que hayas escrito bien los nombres y en minúscula")
    sys.exit("O quizá escribiste algo que no era un planeta del sistema solar")

velocidad = ( (2*G*M) / R )**(1/2.)
vKilometros = velocidad / 1000
print(f"La velocidad que debe alcanzar su objeto para escapar de la tierra es de {velocidad} metros por segundo")
print(f"Además, esa velocidad en kilómetros por segundo es de {vKilometros}")