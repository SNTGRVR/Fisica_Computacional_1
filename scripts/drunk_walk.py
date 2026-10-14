import math
import random
import matplotlib.pyplot as plt
import numpy as np


def drunk_1d(N, L=1.0):
    """
    Simula caminantx aleatorio en 1D.
    Paso Δx ~ [-L, L].
    """
    x = 0.0 #centrado en 0
    x_history = [x]

    for _ in range(N): #note que no uso el contador i porque no lo necesito
        x += (random.random() - 0.5) * 2.0 * L # paso aleatorio entre -1 y 1
        x_history.append(x)

    return x_history


def drunk_2d(N, L=1.0):
    """
    Simula caminantx aleatorio en 2D.
    Pasos independientes Δx, Δy ~ [-L, L].
    """
    x, y = 0.0, 0.0
    x_history, y_history = [x], [y]

    for _ in range(N):
        x += (random.random() - 0.5) * 2.0 * L
        y += (random.random() - 0.5) * 2.0 * L
        x_history.append(x)
        y_history.append(y)

    return x_history, y_history

def drunk_3d(N, L=1.0):
    """
    Simula caminantx aleatorio en 3D.
    Pasos independientes Δx, Δy, Δz ~ [-L, L].
    """
    x, y, z = 0.0, 0.0, 0.0
    x_history, y_history, z_history = [x], [y], [z]

    for _ in range(N):
        x += (random.random() - 0.5) * 2.0 * L
        y += (random.random() - 0.5) * 2.0 * L
        z += (random.random() - 0.5) * 2.0 * L
        x_history.append(x)
        y_history.append(y)
        z_history.append(z)

    return x_history, y_history, z_history 


if __name__ == "__main__":

    # ---------------------------------------------------------
    # PARÁMETROS GENERALES
    # ---------------------------------------------------------
    N = 1000  # Número total de pasos
    L = 10.0
    n_pasos = list(range(N + 1))
    semilla =42

    random.seed(semilla) 
    np.random.seed(semilla)

    # 1D
    x_1d = drunk_1d(N, L=L)
    x_final_1d = x_1d[-1]
    
    # 2D
    x_2d, y_2d = drunk_2d(N, L=L)
    x_final_2d, y_final_2d = x_2d[-1], y_2d[-1]
    
    # 3D
    x_3d, y_3d, z_3d = drunk_3d(N, L=L)
    x_final_3d, y_final_3d, z_final_3d = x_3d[-1], y_3d[-1], z_3d[-1]
    
    # ---------------------------------------------------------
    # PLOTS 
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(15, 4))

    # --- Subplot 1: Random Walk 1D (x vs Tiempo/Pasos) ---
    ax1 = fig.add_subplot(1, 3, 1)
    ax1.plot(n_pasos, x_1d, color='royalblue', linewidth=1.5, label='Trayectoria $x(N)$')
    ax1.plot(0, x_1d[0], 'go', markersize=7, label='Inicio')
    ax1.plot(N, x_final_1d, 'ro', markersize=7, label='Fin')

    ax1.set_title('Random Walk 1D', fontweight='bold')
    ax1.set_xlabel('Número de pasos ($N$)')
    ax1.set_ylabel('Posición $x$')
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.legend(loc='upper left', fontsize=9)

    # --- Subplot 2: Random Walk 2D (Plano X-Y) ---
    ax2 = fig.add_subplot(1, 3, 2)
    ax2.plot(x_2d, y_2d, color='royalblue', linewidth=1, alpha=0.85, label='Trayectoria')
    ax2.plot(0, 0, 'go', markersize=8, label='Inicio (0,0)')
    ax2.plot(x_final_2d, y_final_2d, 'ro', markersize=8, label='Fin')

    ax2.set_title('Random Walk 2D', fontweight='bold')
    ax2.set_xlabel('Posición $x$')
    ax2.set_ylabel('Posición $y$')
    ax2.set_aspect('equal', 'datalim')
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.legend(loc='upper right', fontsize=9)

    # --- Subplot 3D: Espacio X-Y-Z ---
    ax3 = fig.add_subplot(1, 3, 3, projection='3d')
    ax3.plot(x_3d, y_3d, z_3d, color='royalblue', linewidth=1, alpha=0.85, label='Trayectoria')
    ax3.plot([0], [0], [0], 'go', markersize=7, label='Inicio (0,0,0)')
    ax3.plot([x_3d[-1]], [y_3d[-1]], [z_3d[-1]], 'ro', markersize=7, label='Fin')

    ax3.set_title('Random Walk 3D', fontweight='bold')
    ax3.set_xlabel('Posición $x$')
    ax3.set_ylabel('Posición $y$')
    ax3.set_zlabel('Posición $z$')
    ax3.legend(loc='upper right', fontsize=8)

    fig.tight_layout()
    plt.savefig('../Clases/Herramientas_Python/drunk.pdf', bbox_inches='tight')

    plt.show()