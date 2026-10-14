""" 
fibonacci. py
Es un módulo que genera los números de Fibonacci y se verifica la famosa razón aúrea. 
"""
import math 

def Fibonacci(N):
    """
    Genera y devuelve una lista  con los primeros N números de Fibonacci.
    
    Parametros de entrada:
    N (int): Número de Fibonacci que desea generar.
    
    Devuelve:
    list: Los primeros N números de Fibonacci comenzando desde f_1 = 1 y f_2 = 1.
    """
    if N <= 0:
        print("Error: N debe ser un entero positivo.")
        return []
    elif N == 1:
        return [1]
    
    # Inicia la secuencia (lista) con los dos primeros números 
    fib_sequence = [1, 1]
    
    # Agrego los números de Fibonacci hasta que la longitud de la lista sea N, con el .append
    # Tomamos el último de la lista fib_sequence[-1] 
    # Tomamos el penúltimo de la lista fib_sequence[-2] 
    # Agregamos cada elemento a la lista fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    # Devuelve la lista desde e primero hasta el N-1 fib_sequence[:N]
    for i in range(2, N):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        
    return fib_sequence[:N]

def convergencia(F):
    """
    Acá chequeamos la convergencia de la sucesión de Fibonacci y comparamos 
    con la razón aúrea.
    
    Paramétro de entrada: La lista F con los números de Fibonacci.
    
    Retorna:
    None: Imprime una tabla con la comparación entre la convergencia de la 
    sucesión de fibonacci y la razón aúrea.
    """
    # La rázon aúrea: (1 + sqrt(5)) / 2
    aurea = (1 + math.sqrt(5)) / 2
    
    # Se necesitan al menos dos números de Fibonacci para calcular la razón
    valid_fibs = [x for x in F if x > 0]
    
    if len(valid_fibs) < 2:
        print("Error: La lista de entrada debe contener al menos dos números de Fibonacci.")
        return

    print(f"{'n':<5} | {'f_n':<10} | {'f_n+1':<10} | {'Razón (F_n+1 / F_n)':<22} | {'Diferencia con la razón aúrea':<30}")
    print("-" * 85)

    ratios = []
    for i in range(len(valid_fibs) - 1):
        fn = valid_fibs[i]
        fn1 = valid_fibs[i+1]
        ratio = fn1 / fn
        ratios.append(ratio)
        diff = abs(ratio - aurea)
        
        print(f"{i+1:<5} | {fn:<10} | {fn1:<10} | {ratio:<22.10f} | {diff:<30.10e}")

    # Chequea si la última diferencia es cercana a 0
    final_diff = abs(ratios[-1] - aurea)
    print("\n" + "=" * 85)
    print(f"Razón aúrea (Valor real): {aurea:.10f}")
    print(f"Última razón calculada:     {ratios[-1]:.10f}")
    print(f"Discrepancia absoluta:      {final_diff:.10e}")
    
    if final_diff < 1e-4:
        print("\nVerdicto: Johannes Kepler estaba correcto! .")
    else:
        print("\nVerdicto: La secuencia es demasiado corta para mostrar una convergencia.")


# --- Programa principal ---
if __name__ == "__main__":

    print("--- Test Block del programa fibonacci.py ---\n")
    N = int(input("Ingrese el número de términos para la secuencia "))

    print(f"Generando los primeros {N} números de Fibonacci:")

    fib_list = Fibonacci(N)
    print(fib_list)
    print("\n" + "=" * 85 + "\n")
    
    print("Verificando la convergencia :")
    convergencia(fib_list)