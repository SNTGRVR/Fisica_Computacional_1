import matplotlib.pyplot as plt
import numpy as np


def monte_carlo_pi(N=5000, seed=42):
  rng = np.random.default_rng(seed)
  x = rng.uniform(-1, 1, N)
  y = rng.uniform(-1, 1, N)
  adentro = x**2 + y**2 <= 1.0 # se define el disco de radio 1
  M = np.sum(adentro) # suma todos los puntos adentro del círculo
  pi_ran = 4.0 * M / N
  return x, y, adentro, pi_ran, M


if __name__ == "__main__":
  N = 5000
  x, y, adentro, pi_aprox, M = monte_carlo_pi(N)

  plt.figure(figsize=(6, 6), facecolor='white')
  plt.scatter(x[adentro], y[adentro], s=2, color="crimson")
  plt.scatter(x[~adentro], y[~adentro], s=2, color="blue", alpha=0.4)

  # Frontera
  theta = np.linspace(0, 2 * np.pi, 200)
  plt.plot(np.cos(theta), np.sin(theta), "k-", lw=1.5)

  plt.axis("equal")
  plt.xlim(-1.05, 1.05)
  plt.ylim(-1.05, 1.05)
  plt.title(f"Monte Carlo: $\\pi \\approx {pi_aprox:.4f}$ (N = {N}) (M = {M})")
  plt.tick_params (axis='both', which='both', labelsize =12)
  plt.tight_layout()
  plt.savefig('../Clases/Herramientas_Python/pirandom.pdf', bbox_inches='tight')

  plt.show()