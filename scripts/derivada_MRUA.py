import numpy as np

def x(t, x0=0., v0 = 0., a=2.5):
    'MRUA'
    return x0 + v0*t + 1/2. *a*t**2 

t = np.linspace(0,100,10)
x0 = float(input("Ingrese la posición inicial en m\n"))
v0 = float(input("Ingrese la velocidad inicial en m/s\n"))
a  = float(input("Ingrese la aceleración inicialen m0/s^2\n"))

r = x(t,x0,v0,a)

# velocidad v(t) = dx/dt
v_num = np.gradient(r, t)
# aceleración a(t) = dv/dt 
a_num = np.gradient(v_num, t)


v_num2 = np.gradient(r, t, edge_order=2)
a_num2 = np.gradient(v_num2, t, edge_order=2)

# velocidad analítica v(t) = v0 + a * t = 2.5 * t
v_exacta = v0 + a*t
# aceleración analítica a(t) = a 
a_exacta = a    

print("\n" + "="*50)
print("Velocidad exacta:    \n", np.round(v_exacta, 2))
print("Velocidad numérica:  \n", np.round(v_num, 2))
print("-" * 50)
print("Aceleración exacta:  \n", a_exacta)
print("Aceleración numérica:\n", np.round(a_num, 2))
print("="*50)
print("Velocidad numérica edge_order2:  \n", np.round(v_num2, 2))
print("-" * 50)
print("Aceleración numérica edge_order2:\n", np.round(a_num2, 2))
print("="*50)