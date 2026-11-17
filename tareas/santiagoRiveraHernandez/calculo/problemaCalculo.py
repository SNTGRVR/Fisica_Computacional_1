import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd

"""E(x) = integral de 0 a x de [(e^-t^2)dt]"""

columnas = {
    "x":        [],
    "E(x)":     [],
    "error":    [],
}

tabla = pd.DataFrame(columnas)
tabla["x"] = np.arange(0, 3.1, 0.1)

f = lambda t: np.exp(-t**2)
intequad = tabla["x"].apply(
    lambda x: sp.integrate.quad(f, 0, x)
)

tabla["E(x)"] = intequad.apply(lambda resultado: resultado[0])
tabla["error"] = intequad.apply(lambda resultado: resultado[1])

print(tabla)

"""Primer numeral hecho, ahora el segundo"""

plt.figure(figsize=(6, 4))
plt.plot(tabla["x"], tabla["E(x)"], marker="*", label="E(x)")
plt.axhline(y=(np.pi)**(0.5)/2, color="red", ls="-.", lw=1, label="Asíntota")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("E(x)")
plt.title("Integral de exponencial en función de x")
plt.legend(loc="lower right")
plt.show()