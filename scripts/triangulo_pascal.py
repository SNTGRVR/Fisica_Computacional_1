""" Lee la función factorial, calcula la combinatoria y muestra el triángulo 
de Pascal"""

import factorial_v2  as fa # importamos nuestra función

def binomial(n, k):
    """
    Calcula el coeficiente binomial C(n, k) = n! / (k! * (n - k)!)
    usando la función factorial previamente definida.
    Retorna un número entero.
    """
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    # Usamos la función factorial que llamamos 
    num = fa.factorial(n)
    den = fa.factorial(k) * fa.factorial(n - k)
    return int(num/den)

def imprimir_pascal(filas):
    """Imprime las primeras filas del Triángulo de Pascal."""
    for n in range(filas):
        linea = []
        for k in range(n + 1):
            # Llamamos a la función de coeficientes binomial(n, k)
            coeficiente = binomial(n, k)
            linea.append(str(coeficiente))
        
        # Unir los números con espacios sin centrar
        #print(" ".join(linea))
        # Centra el texto en un ancho fijo de 40 caracteres
        print(" ".join(linea).center(40))

if __name__ == "__main__":

    # Pedir las filas que desee del triángulo de Pasca
    n = int(input("¿Cuántas filas desea para el triángulo?\t"))
    imprimir_pascal(n)
