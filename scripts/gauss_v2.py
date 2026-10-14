""" En este programa se comprueba la suma de Gauss usando el for"""

print("comprobación de la fórmula de Gauss:\n")
print("1+2+3+....+100 =5050\n")

suma = 0  #inicaimos el acumulador de lasuma

for i in range(1,101,1):
    suma = suma + i # recuerde que puede usar suma += i

print(f"El valor de la suma es: {suma} ")
