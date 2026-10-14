import numpy as np
import matplotlib.pyplot as plt

def lcg(size, seed=23):
    """Genera un arreglo de N número entre (0,1) usando xn+1 = axn + c mod m"""
    a = 1103515245 
    c = 12345
    m = 2**31

    numeros = np.empty(size)
    x0 = seed
    xn = x0
    
    for i in range(size):
        xn = (a*xn + c) % m
        numeros[i] = xn/m
    return numeros

if __name__== "__main__":

    N = 10000 
    semilla = 12

    #datos a mano con Linear congruence
    datos_lcg = lcg(N,semilla) * 1000

    # datos con numpy 
    rng = np.random.default_rng(seed=semilla) # instanciamos semilla
    datos_numpy = rng.random(N) * 1000

    # 3. Scatter Plots 
    fig, axes = plt.subplots(1, 2, figsize=(11, 5))

    # Scatter LCG (A mano)
    axes[0].scatter(datos_lcg[:-1], datos_lcg[1:], s=1, color='crimson', alpha=0.5)
    axes[0].set_title("Correlación $x_n$ vs $x_{n+1}$ (A mano - LCG)", fontweight='bold',fontsize=15)
    axes[0].set_xlabel("$x_n$",fontsize=18)
    axes[0].set_ylabel("$x_{n+1}$",fontsize=18)

    # Scatter NumPy
    axes[1].scatter(datos_numpy[:-1], datos_numpy[1:], s=1, color='teal', alpha=0.5)
    axes[1].set_title("Correlación $x_n$ vs $x_{n+1}$ (NumPy - PCG64)", fontweight='bold',fontsize=15)
    axes[1].set_xlabel("$x_n$",fontsize=18)
    #axes[1].set_ylabel("$x_{n+1}$",fontsize=18)

    plt.tight_layout()

    plt.savefig("../Clases/Herramientas_Python/random.pdf", bbox_inches='tight')
    plt.show()