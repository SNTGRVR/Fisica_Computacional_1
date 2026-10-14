""" En este programa se comprueba la suma de Gauss"""
print("comprobación de la fórmula de Gauss:\n")
print("1+2+3+....+100 =5050\n")

k = 1     #iniciamos contador
suma = 0  #inicaimos el acumulador de lasuma

while k <=  100:
    suma = suma + k # recuerde que puede usar suma += k
    k += 1 # k = k+1

print(f"El valor de la suma es: {suma} ")
