""" En este programa se comprueba la suma de Gauss usando el for
Se pide ingresar el número de términos en la suma"""

print("----------------------------------------")
print("comprobación de la fórmula de Gauss:\n")
print("1+2+3+....+n = n(n+1)/2\n")
print("----------------------------------------")

try:
    N = int(input("Ingrese el número de términos N que desea sumar: "))
    if N < 1:
        # Le decimos que N<1 es un error también (yo genero la alarma)
        raise ValueError("N debe ser mayor o igual que 1") 

except ValueError: 
    print(f"Error: No puede ingrdar letras ni números menores que 1")

else:
    k = 1 # inicamos el contador 
    suma = 0  #inicaimos el acumulador de lasuma

    for i in range(1,N+1,1):
        suma = suma + i # recuerde que puede usar suma += i

    teorico = int(N * (N + 1)/2)
    print(f"El valor de la suma es: {suma} ")
    print(f"El valor teórico de la suma es: {teorico} ")