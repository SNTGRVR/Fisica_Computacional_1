import numpy as np
import matplotlib.pyplot as plt

N =  1000 # número de úntos
x = np.linspace(-20,20,N)

y = np.tan(x) 

dy = 1 / np.cos(x)**2 # derivada exacta de tan(x)

# derivadas numéricas
dy1 =  np.gradient(y, x, edge_order=1) 
dy2 =  np.gradient(y, x, edge_order=2)

# errores
error1 = np.abs(dy - dy1)
error2 = np.abs(dy - dy2)

#plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

# Subplot 1: Función y derivadas
ax1.plot(x, y, "k--", alpha=0.5, lw = 2,label=r"$f(x) = \tan(x)$")
ax1.plot(x, dy, "k-", lw=2, label=r"Analítica: $\sec^2(x)$")
ax1.plot(x, dy1, "ro", markersize=5, label=r"Numérica (edge_order=1)")
ax1.plot(x, dy2, "b.", markersize=4, label=r"Numérica (edge_order=2)")
ax1.set_ylim(0, 20)
ax1.grid(True, ls=":", alpha=0.6)
ax1.legend(loc="upper right", fontsize=18)
ax1.tick_params (axis='both', which='both', labelsize =20)

# Subplot 2: Error absoluto
ax2.semilogy(x, error1, "r-o", markersize=4, label=r"Error $|f'_{exacta} - f'_{num}|$ (edge=1)")
ax2.semilogy(x, error2, "b-s", markersize=4, label=r"Error $|f'_{exacta} - f'_{num}|$ (edge=2)")
ax2.set_xlabel(r"$x$ (rad)", fontsize=20)
ax2.set_ylabel("Error absoluto", fontsize=20)
ax2.grid(True, which="both", ls=":", alpha=0.6)
ax2.legend(loc="lower center", fontsize=18)
ax2.tick_params (axis='both', which='both', labelsize =20)

plt.tight_layout()
plt.show()