""" Nuestro primer programa en Python. 
Modificado con el condicional if"""

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
if edad < 0:
    print("Tu edad debe ser positiva, suerte llave")
else:
    print(f"-------------------------------")
    # Hacemos operaciones con ese entero 
    edad_segundos = edad * 365 * 24 * 3600 #calcula edad en segundos
    edad_minutos = edad * 365 * 24 * 60 #calcula edad en minutos
    futura_edad = edad + 5 # edad dentro de 5 años
    print(f"Tu edad en minutos es {edad_minutos}. En notación científica es {edad_minutos:.2e} minutos")
    print(f"Tu edad en segundos es {edad_segundos}. En notación científica es {edad_segundos:.2e} segundos")
    print(f"Si todo sale bien, te graduarías de Física a los {futura_edad} años.")
    print("-----------------------------------------")
