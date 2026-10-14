""" Nuestro primer programa en Python. 
Pregunta algunos datos personales"""

# con el comando print(""), imprimimos un mensaje en cosa \n salta la linea
print("¡Hola, espero que te encuentres muy bien!")

#El comando input se utiliza para ingresar información. 
#Por defecto la variable asigada es un string
nombre = input("¿Cuál es tu nombre?\n")

print(f"-------------------------------")
# Uso de f-strings para la salida
print(f"¡Mucho gusto, {nombre}!")

# Conversión de datos. 
# int() convierte la entrada a un entero
print(f"-------------------------------")
edad= int(input("¿Cuántos años tienes?\n"))
print(f"-------------------------------")
# Hacemos operaciones con ese entero 
edad_segundos = edad * 365 * 24 * 3600 #calcula edad en segundos
edad_minutos = edad * 365 * 24 * 60 #calcula edad en minutos
futura_edad = edad + 5 # edad dentro de 5 años
print(f"Tu edad en minutos es {edad_minutos}. En notación científica es {edad_minutos:.2e} minutos")
print(f"Tu edad en segundos es {edad_segundos}. En notación científica es {edad_segundos:.2e} segundos")
print(f"Si todo sale bien, te graduarías de Física a los {futura_edad} años.")
print("-----------------------------------------")

#EDAD DEL UNIVERSO
# Edad del universo aproximada en años (13 800 millones de años)
edad_universo = 13.8e9  # Notación científica en Python para float
edad_universo_segundos = edad_universo * 365.25 * 24 * 3600 # edad universo en segundos

# Calculamos el porcentaje que representa la edad de entrada respecto a la del Universo
porcentaje = (edad / edad_universo) * 100

print(f"Por otro lado, la edad del universo es de {edad_universo:.2e} años,")
print(f"lo cual equivale a aproximadamente: {edad_universo_segundos:.2e} segundos.")
print(f"Eso significa que has vivido aproximadamente el {porcentaje:.10f}% de la historia del universo.")
print("-------------------------------")

# EDAD DE LA TIERRA
edad_tierra = 4.54e9   # Edad de la Tierra aproximada en años (4540 millones de años)
edad_tierra_segundos = edad_tierra * 365.25 * 24 * 3600 # Edad de la Tierra en segundos

# Calculamos el porcentaje que representa la edad de entrada respecto a la Tierra
porcentaje_tierra = (edad / edad_tierra) * 100

print(f"Además, la edad de la Tierra es de {edad_tierra:.2e} años ({edad_tierra_segundos:.2e} segundos).")
print(f"Has presenciado aproximadamente el {porcentaje_tierra:.8f}% de la existencia de nuestro planeta.")
print("-------------------------------")

# 3. APARICIÓN DEL HOMO SAPIENS
edad_humanidad = 300000.0  # 300 000 años aproximadamente
edad_humanidad_segundos = edad_humanidad * 365.25 * 24 * 3600

porcentaje_humano_universo = (edad_humanidad / edad_universo) * 100
porcentaje_humano_tierra = (edad_humanidad / edad_tierra) * 100

print(f"En perspectiva evolutiva, los primeros Homo sapiens aparecieron hace {edad_humanidad} años.")
print(f"En segundos, la humanidad lleva existiendo aproximadamente {edad_humanidad_segundos:.2e} s (~10^13 s).")
print(f"- Nuestra especie solo representa el {porcentaje_humano_tierra:.4f}% de la historia de la Tierra.")
print(f"- Respecto al universo, la humanidad solo abarca el {porcentaje_humano_universo:.5f}% de su historia.")
print("-------------------------------")
print("-------------------------------")