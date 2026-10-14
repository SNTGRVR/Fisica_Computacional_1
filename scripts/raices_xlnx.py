import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x + np.log(x)

def df(x):
    return 1 + 1/x

x = np.linspace(0.01, 10, 100)
fx = f(x)

plt.figure(figsize=(8, 5))
plt.plot(x, x, color='blue', lw=2, label=rf'$f(x) = x$' )
plt.plot(x, -np.log(x), color='red', linestyle='--', label=rf'$f(x)= - \ln({{x}})  $',lw=2)
plt.ylabel(r'$f(x)$',fontsize=15)
plt.xlabel(r'$x$ ',fontsize=15)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=15)
plt.tight_layout()

sol_brent = sp.optimize.root_scalar(f, bracket=[0.1, 1.0], method='brentq')
sol_secante = sp.optimize.root_scalar(f, x0=1.0, method='secant')
sol_bisect  = sp.optimize.root_scalar(f, bracket=[0.1, 1.0], method='bisect',xtol=1e-8)
sol_newton  = sp.optimize.root_scalar(f, x0=1.0, fprime=df, method='newton')
sol_lambert = np.real(sp.special.lambertw(1))

metodos = [
    ("Brent (brentq)", sol_brent.root, sol_brent.iterations, sol_brent.function_calls),
    ("Bisección", sol_bisect.root, sol_bisect.iterations, sol_bisect.function_calls),
    ("Secante", sol_secante.root, sol_secante.iterations, sol_secante.function_calls),
    ("Newton", sol_newton.root, sol_newton.iterations, sol_newton.function_calls),
    ("Lambert W", sol_lambert, 1, 1)
]

print(f"{'Método':<18} | {'Raíz Hallada':<14} | {'Residuo f(x)':<14} | {'Iteraciones':<12} | {'Llamadas f(x)':<14}")
print("-" * 80)
for nombre, raiz, iters, nfev in metodos:
    residuo = abs(f(raiz))
    print(f"{nombre:<18} | {raiz:<14.8f} | {residuo:<14.2e} | {iters:<12} | {nfev:<14}")

plt.savefig('../Clases/Herramientas_Python/xlnx.pdf', bbox_inches='tight')
plt.show()