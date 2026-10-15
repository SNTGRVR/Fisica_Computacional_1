# Un logaritmo es una función que nos da el valor al que hay que elevar una base para obtener un número, es una función adivinadora xd.
    # Pero debe haber una manera de hacerlo de forma sencilla, sino que como es la 1 de la mañana, pues mi cerebro no está precisamente en su peak
    # log b(x) = y
    # log 10(0.1) = -1 porque 10/10/10 = 0.1, ergo 10^(-1) = 0.1
    # log 10(1) = 0 porque 10 / 10 = 1, ergo 10^0 = 1
    # log 10(10) = 1 porque 10 = 10, ergo 10^1 = 10
    # log 10(100) = 2 porque 10 * 10 = 100, ergo 10^2 = 100
    # Se me ocurre hacer algo que, cuando b sea mayor a x, divida, y cuando b sea menor a x multiplique, ¿debería definir y con anticipación
    # Pero para empezar, el logaritmo no se le puede calcular a un número negativo ni a cero
def logBase(b, x):
    import math
    if x <= 0:
        print("No existe en los números reales")
        return None
    elif b <= 0 or b == 1:
        print("La base debe ser positiva y distinta de 1")
        return None
    else:
        return math.log(x, b)