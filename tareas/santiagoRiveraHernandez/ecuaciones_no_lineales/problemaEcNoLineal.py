import matplotlib.pyplot as plt
import scipy as sp
import numpy as np

x = np.linspace(-2, 2, 100)

def f(x):
    return 2 -np.e**(-x) -x
def g(x):
    return np.e**(-x) -2*x -x**(3)
def h(x):
    return np.cos(x) -x

plt.figure(figsize=(6, 4))
plt.plot(x, f(x), color="yellow", label="función 1")
plt.plot(x, g(x), color="blue", label="función 2")
plt.plot(x, h(x), color="red", label="función 3")
plt.axvline(0, color='brown', lw=0.6, alpha=0.5)
plt.axhline(0, color='brown', lw=0.6, alpha=0.5)
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

"""El método gráfico me muestra en qué intervalos están las raíces"""

#intervalos f(X): [-2, -1], [1, 2]
#intervalo g(x): [0, 1]
#intervalo h(x): [0, 1]

solF1 = sp.optimize.root_scalar(f, bracket=[-2, -1], method='brentq')
solF2 = sp.optimize.root_scalar(f, bracket=[1, 2], method='brentq')
solG = sp.optimize.root_scalar(g, bracket=[0, 1], method='brentq')
solH = sp.optimize.root_scalar(h, bracket=[0, 1], method='brentq')

print("intervalo 1 f(x): ", solF1.root, solF1.iterations, solF1.function_calls)
print("intervalo 2 f(x): ", solF2.root, solF2.iterations, solF2.function_calls)
print("intervalo g(x): ", solG.root, solG.iterations, solG.function_calls)
print("intervalo h(x): ", solH.root, solH.iterations, solH.function_calls)