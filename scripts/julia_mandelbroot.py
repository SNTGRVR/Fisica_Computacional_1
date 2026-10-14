import matplotlib.pyplot as plt
import numpy as np


def mandelbrot(xmin=-2.0, xmax=0.5, ymin=-1.25, ymax=1.25, width=1000, height=1000, max_iter=200):
  """Calcula la matriz para el Conjunto de Mandelbrot.
  Mantiene z0 = 0 y varía c.
  
  Parámetros:

  xmin, xmax: rango para el eje horizopntal. parte real de c
  ymin, ymax = rango para el eje vertical. parte imaginaria de c
  width, height: resolución de la imagen (por defecto $1000 \times 1000 = 10^6$ puntos).
  max_iter: El límite de iteraciones por punto. Si desíés de 200 pasos |z|<2 se asume que 
  pertenece al conjunto de Mandelbrot.

  Devuelve:

  escape_grid: Una matriz 2D de enteros de tamaño (height, width). Cada celda (i, j) 
  almacena el número de iteraciones en las que ese punto escapó 
  (un valor entre $0$ y $199$), o $200$ (max_iter) si el punto nunca escapó y 
  se quedó atrapado dentro del fractal.

  (xmin, xmax, ymin, ymax): Una tupla con las coordenadas extremas. 
  Estas se usan para graficar con plt.imshow y graficar los valores físicos en lugar del 
  índice de píxeles del arreglo.
  """

  x = np.linspace(xmin, xmax, width)
  y = np.linspace(ymin, ymax, height)
  C = x + 1j * y[:, None]  # Matriz de parámetros c La coma crea una segunda dimensión en el array
  Z = np.zeros_like(C, dtype=np.complex128) # se crea la martriz de ceros con la dimensión de C
  escape_grid = np.full(C.shape, max_iter, dtype=int) # matriz para enviar a imshow

  # Máscara para rastrear los puntos con |z| <= 2 
  mask = np.ones(C.shape, dtype=bool)

  for i in range(max_iter):
    Z[mask] = Z[mask] ** 2 + C[mask] #aplicamos la ecuación z = z**2 +c para la mascara true
    escaped = np.abs(Z) > 2.0 # True si no pertenecen al conjunto, False si sí pertenece
    newly_escaped = escaped & mask
    escape_grid[newly_escaped] = i
    mask &= ~escaped # los puntos que quedan, se niegan los que no estan
    if not np.any(mask):
      break

  return escape_grid, (xmin, xmax, ymin, ymax)


def julia(c, xmin=-1.5, xmax=1.5, ymin=-1.5, ymax=1.5, width=1000, height=1000, max_iter=200):
  """Calcula la matriz para un Conjunto de Julia fijado en c.
  Mantiene c constante y varía las condiciones iniciales z0.

  Parámetros:
  
   xmin, xmax: rango para el eje horizopntal. parte real de c
   ymin, ymax = rango para el eje vertical. parte imaginaria de c
   width, height: resolución de la imagen (por defecto $1000 \times 1000 = 10^6$ puntos).
   max_iter: El límite de iteraciones por punto. Si desíés de 200 pasos |z|<2 se asume que 
   pertenece al conjunto de Mandelbrot.
  
  Devuelve:
  escape_grid: Una matriz 2D de enteros de tamaño (height, width). Cada celda (i, j) 
  almacena el número de iteraciones en las que ese punto escapó 
  (un valor entre $0$ y $199$), o $200$ (max_iter) si el punto nunca escapó y 
  se quedó atrapado dentro del fractal.
  (xmin, xmax, ymin, ymax): Una tupla con las coordenadas extremas. 
  Estas se usan para graficar con plt.imshow y graficar los valores físicos en lugar del 
  índice de píxeles del arreglo.
   """
  
  x = np.linspace(xmin, xmax, width)
  y = np.linspace(ymin, ymax, height)
  Z = x + 1j * y[:, None]  # Matriz de condiciones iniciales z0
  escape_grid = np.full(Z.shape, max_iter, dtype=int)

  mask = np.ones(Z.shape, dtype=bool)

  for i in range(max_iter):
    Z[mask] = Z[mask] ** 2 + c
    escaped = np.abs(Z) > 2.0
    newly_escaped = escaped & mask
    escape_grid[newly_escaped] = i
    mask &= ~escaped
    if not np.any(mask):
      break

  return escape_grid, (xmin, xmax, ymin, ymax)

if __name__ == "__main__":
  
  #c_interesante = -0.7 + 0.27015j
  #c_interesante = -0.75 + 0.0j
  #c_interesante = 0.285 + 0.01j
  c_interesante = -0.8 + 0.156j
  # Genera matrices numéricas
  grid_mandelbrot, ext_m = mandelbrot(max_iter=300)
  grid_julia, ext_j = julia(c=c_interesante, max_iter=300)

  # plot
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), facecolor="black")

  # Mandelbrot Plot
  ax1.imshow(grid_mandelbrot, extent=ext_m, cmap="twilight_shifted", origin="lower" )
  ax1.set_title("Conjunto de Mandelbrot", color="white", fontsize=15,fontweight="bold")
  ax1.set_xlabel("Re(c)", color="white",fontsize=16, labelpad=8)
  ax1.set_ylabel("Im(c)", color="white", fontsize=16, labelpad=8)
  ax1.tick_params(axis="both", which="major", labelsize=13, colors="white")

  # Julia Plot
  ax2.imshow(grid_julia, extent=ext_j, cmap="twilight_shifted", origin="lower")
  ax2.set_title( f"Conjunto de Julia para $c = {c_interesante}$", color="white", fontsize=15,fontweight="bold")
  ax2.set_xlabel("Re($z_0$)", color="white",fontsize=16, labelpad=8)
  ax2.set_ylabel("Im($z_0$)", color="white",fontsize=16, labelpad=8)
  ax2.tick_params(axis="both", which="major", labelsize=13, colors="white")

  plt.tight_layout()
  plt.savefig('../Clases/Herramientas_Python/julia_manderboot.pdf', bbox_inches='tight')
  plt.show()