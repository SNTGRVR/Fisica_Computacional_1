import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(xmin=-2, xmax=2, ymin=-2, ymax=2, width=500, height=500, max_iter=100):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    C = x + 1j * y[:, None]
    Z = np.zeros_like(C, dtype=np.complex128)
    escape_grid = np.full(C.shape, max_iter, dtype=int)
    mask = np.ones(C.shape, dtype=bool)

    for i in range(max_iter):
        Z[mask] = Z[mask]**2 + C[mask]
        escaped = np.abs(Z) > 2.0
        newly_escaped = escaped & mask
        escape_grid[newly_escaped] = i
        mask &= ~escaped
        if not np.any(mask):
            break

    return escape_grid, (xmin, xmax, ymin, ymax)

escape_grid, limites = mandelbrot()

plt.imshow(
    escape_grid,
    extent=limites,
    origin='lower',
    cmap='hot'
)

plt.colorbar(label='Iteraciones')
plt.xlabel('Parte real')
plt.ylabel('Parte imaginaria')
plt.title('Conjunto de Mandelbrot')
plt.show()