import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("resultados_C.csv")

data["n"] = data["MV"] / data["mN1"]
data["CanalDecaimiento"] = np.where(
    data["n"] >= 2.0, "Permitido", "Bloqueado"
)

data["DMRegime"] = np.where(
    data["Gamma_over_H"] < 1.0, "FIMP", "WIMP"
)

FIMP = data[data["DMRegime"] == "FIMP"]
WIMP = data[data["DMRegime"] == "WIMP"]

print(data)
print("=" * 60)
data.info()
print("=" * 60)

porcentajeFIMP = (
    (FIMP["CanalDecaimiento"] == "Bloqueado").sum()
    / len(FIMP) * 100
)

porcentajeWIMP = (
    (WIMP["CanalDecaimiento"] == "Bloqueado").sum()
    / len(WIMP) * 100
)

print(f"Porcentaje de puntos FIMP con canal bloqueado: {porcentajeFIMP:.3f}%")
print(f"Porcentaje de puntos WIMP con canal bloqueado: {porcentajeWIMP:.3f}%")
