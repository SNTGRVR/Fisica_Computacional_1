import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def drunk_nd(N, dim=1, L=1.0):
    """
    Simula la caminata en 1D, 2D o 3D con el algoritmo vectorizado.

    Parámetros:
    -----------
    N : int->Número total de pasos (N).
    dim  : int, opcional (1, 2 o 3)
    -> Dimensión del espacio de caminata (por defecto es 1).
    L : float, opcional
    -> Semi-amplitud del paso en cada eje: Δk ~ [-L, L] (por defecto es 1.0).
        
    Retorna:
    --------
    trayectoria : numpy.ndarray
        Matriz de forma (jmax + 1, dim) con la secuencia de posiciones.
        Para dim = 1 retorna un arreglo 1D de forma (jmax + 1,).
    """
    if dim not in (1, 2, 3):
        raise ValueError("El parámetro 'dim' debe ser 1, 2 o 3.")
    
    # Genera la matriz de pasos aleatorios continuos Δk ~ [-L, L] de forma (jmax, dim)
    pasos = np.random.uniform(-L, L, size=(N, dim))
    
    # Posición inicial en el origen: (1, dim) de ceros
    origen = np.zeros((1, dim))
    
    # Concatena el origen al inicio y calcula la suma acumulada a lo largo del tiempo (eje 0)
    trayectoria = np.vstack([origen, np.cumsum(pasos, axis=0)])
    
    # Si dim=1, aplanamos para devolver un arreglo 1D sencillo (N + 1,)
    if dim == 1:
        return trayectoria.ravel()
        
    return trayectoria

def ejecutar_simulacion(DIM=3, N=100, L=1.0, guardar_gif=False):
  """Ejecuta y anima la simulación de Random Walk en 2D o 3D.

  Parameters:
      DIM (int): Dimensión de la simulación (2 o 3).
      N (int): Número total de pasos.
      L (float): Rango de paso [-L, L].
      guardar_gif (bool): Si es True, guarda el archivo .gif al finalizar.
  """
  # ---------------------------------------------------------
  # GENERACIÓN DE DATOS SEGÚN LA DIMENSIÓN
  # ---------------------------------------------------------
  np.random.seed(42)  # Semilla para reproducibilidad

  traj = drunk_nd(N, dim=DIM, L=L)
  x, y = traj[:, 0], traj[:, 1]
  if DIM == 3:
    z = traj[:, 2]

  #  Volumen del plot
  margin = 2.0
  xlim = (np.min(x) - margin, np.max(x) + margin)
  ylim = (np.min(y) - margin, np.max(y) + margin)

  # ---------------------------------------------------------
  # 3. CONFIGURACIÓN DE LA FIGURA Y EJES
  # ---------------------------------------------------------
  fig = plt.figure(figsize=(9, 7))

  if DIM == 3:
    zlim = (np.min(z) - margin, np.max(z) + margin)
    ax = fig.add_subplot(111, projection="3d")
    ax.set_zlim(zlim)
    ax.set_zlabel("Posición $z$")

    (linea_trayectoria,) = ax.plot(
        [], [], [], color="crimson", linewidth=1.5, alpha=0.85, label="Trayectoria"
    )
    (cabeza_caminante,) = ax.plot(
        [], [], [], "bo", markersize=6, label="Posición actual"
    )
    (marcador_inicio,) = ax.plot(
        [0], [0], [0], "go", markersize=8, label="Inicio (0,0,0)"
    )
    texto_paso = ax.text2D(
        0.02, 0.95, "", transform=ax.transAxes, fontsize=11, fontweight="bold"
    )
  else:
    ax = fig.add_subplot(111)
    ax.grid(True, linestyle="--", alpha=0.5)

    (linea_trayectoria,) = ax.plot(
        [], [], color="crimson", linewidth=1.5, alpha=0.85, label="Trayectoria"
    )
    (cabeza_caminante,) = ax.plot(
        [], [], "bo", markersize=6, label="Posición actual"
    )
    (marcador_inicio,) = ax.plot(
        [0], [0], "go", markersize=8, label="Inicio (0,0)"
    )
    texto_paso = ax.text(
        0.02, 0.95, "", transform=ax.transAxes, fontsize=11, fontweight="bold"
    )

  ax.set_xlim(xlim)
  ax.set_ylim(ylim)
  ax.set_title(
    f"Evolución Temporal de Random Walk {DIM}D", fontweight="bold", fontsize=12
  )
  ax.set_xlabel("Posición $x$")
  ax.set_ylabel("Posición $y$")
  ax.legend(loc="upper right", fontsize=9)

  # ---------------------------------------------------------
  # FUNCIONES DE ANIMACIÓN
  # ---------------------------------------------------------
  def init():
    """Inicializa los elementos gráficos al comienzo de la animación."""
    linea_trayectoria.set_data([], [])
    cabeza_caminante.set_data([], [])
    if DIM == 3:
      linea_trayectoria.set_3d_properties([])
      cabeza_caminante.set_3d_properties([])
    texto_paso.set_text("")
    return linea_trayectoria, cabeza_caminante, texto_paso

  def update(frame):
    """Actualiza la posición del caminante en cada cuadro."""
    linea_trayectoria.set_data(x[: frame + 1], y[: frame + 1])
    cabeza_caminante.set_data([x[frame]], [y[frame]])

    if DIM == 3:
      linea_trayectoria.set_3d_properties(z[: frame + 1])
      cabeza_caminante.set_3d_properties([z[frame]])
      ax.view_init(elev=20, azim=frame * 0.3)

    texto_paso.set_text(f"Paso: {frame} / {N}")
    return linea_trayectoria, cabeza_caminante, texto_paso

  # ---------------------------------------------------------
  # EJECUCIÓN Y EXPORTACIÓN
  # ---------------------------------------------------------
  anim = FuncAnimation(
      fig,
      update,
      frames=len(x),
      init_func=init,
      interval=30,  # Tiempo entre cuadros en ms
      blit=(DIM == 2),  # blit True en 2D, False en 3D
      repeat=False,  # Para no reiniciar al terminar
  )

  if guardar_gif:
    nombre_archivo = f"random_walk_{DIM}d.gif"
    print(f"Guardando animación como {nombre_archivo}...")
    anim.save(nombre_archivo, writer="pillow", fps=30, dpi=100)
    print(f"¡GIF guardado con éxito como '{nombre_archivo}'!")

  plt.show()

if __name__ == "__main__":
  # Cambia DIM a 2 o 3 según lo que quieras simular:
  N = 500
  dim = 2
  L = 2.
  ejecutar_simulacion(DIM=dim, N=N, L=L, guardar_gif=False)