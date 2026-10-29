import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Cargar datos del archivo
datos = np.loadtxt("../data/velocidades.txt")
t = datos[:, 0]  # Tiempo en s
v = datos[:, 1]  # Velocidad en m/s

# Integración: trayectoria acumulada 
# x(t) = integral_0^t v(t') dt'
# initial=0.0 asegura x(t0) = 0 y mantiene la misma dimensión que t
x_acum = sp.integrate.cumulative_trapezoid(v, x=t, initial=0.0)

# Distancia total recorrida
dist_total = sp.integrate.simpson(v, x=t)
print(f"Distancia total recorrida (método de Simpson): {dist_total:.4f} m")

# Derivación: aceleración instantánea a(t) = dv/dt
a_num = np.gradient(v, t, edge_order=2)

# Plots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 9), sharex=True)

# Panel 1: Posición acumulada
ax1.plot(t, x_acum, "tab:red", lw=2, marker="s", markersize=4, label="Posición $x(t) = \\int v dt$")
ax1.set_ylabel("x (m)", fontsize=11)
ax1.grid(True, ls=":", alpha=0.6)
ax1.legend(loc="upper left")

# Panel 2: velocidad
ax2.plot(t, v, "tab:blue", lw=2, marker="o", markersize=4, label="Velocidad experimental $v(t)$")
ax2.set_ylabel("v (m/s)", fontsize=11)
ax2.grid(True, ls=":", alpha=0.6)
ax2.legend(loc="lower left")

# Panel 3: Aceleración 
ax3.plot(t, a_num, "tab:green", lw=2, marker="^", markersize=4, label="Aceleración $a(t) = \\frac{dv}{dt}$ ")
ax3.set_xlabel("Tiempo (s)", fontsize=11)
ax3.set_ylabel("a (m/s$^2$)", fontsize=11)
ax3.grid(True, ls=":", alpha=0.6)
ax3.legend(loc="upper center")

plt.savefig('../lectures/03_herramientas_python/integral_datos.pdf', bbox_inches='tight')

plt.tight_layout()
plt.show()