def cubicroot(N):
    return N**(1/3)

if __name__ == "__main__":
    n = float(input("Ingrese el número al que le quiere sacar raíz cúbica: "))
    nRaiz = cubicroot(n)
    print(f"La raíz cúbica de {n} es: {nRaiz}")