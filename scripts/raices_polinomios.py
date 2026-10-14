import numpy as np
import matplotlib.pyplot as plt

#======= Polinomio: 3x^7 - 4x^5 + 0x^4 + 0x^3 + 6x^2 - x + 3 = 0 ==============

coeff = [3, -1, 6, 0, 0, -4, 0, 3] # note el orden, de menor a mayor
p = np.polynomial.Polynomial(coeff)
raices_p = p.roots()
print("Polinomio:")
print(p)
print("\nRaíces encontradas:")
for i, r in enumerate(raices_p):
    valorevaluado = p(r)
    print(f"  x_{i+1} = {r:.4f}")
    print(f"|residuo|: {abs(valorevaluado):.2e}")

# ===== plot ========
x = np.linspace(-2, 2, 400)
y = np.polyval(coeff, x)
plt.figure(figsize=(10, 7))
plt.plot(x, y, color='red', linestyle='-', label=rf'$p(x)= 3x^7 - 4x^5 + 6x^2 - x + 3 $',lw=2)
plt.xlabel(r'$x$ ',fontsize=20)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=20)
plt.tick_params(axis='both', which='both', labelsize=17) # tamño de los ejes
plt.tight_layout()   
plt.savefig('../Clases/Herramientas_Python/polinomio.pdf', bbox_inches='tight')

plt.show()