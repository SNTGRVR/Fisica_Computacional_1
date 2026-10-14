import numpy as np
import matplotlib.pyplot as plt

# Cargar las columnas directamente en variables independientes
frequency, mic1, mic2 = np.loadtxt('datosmicrofono.txt', unpack=True)

# graficar
plt.figure(figsize=(8, 5))
plt.plot(frequency, mic1, 'r-', label='Micrófono 1')
plt.plot(frequency, mic2, 'b-', label='Micrófono 2')

plt.xlabel('Frecuencia (Hz)',size=15)
plt.ylabel('Amplitud (cm)',size=15)
plt.legend(loc='upper right')
plt.grid(True, ls=':', alpha=0.6)
plt.savefig("../Clases/Introduccion_Python/microfono.pdf")
plt.show()