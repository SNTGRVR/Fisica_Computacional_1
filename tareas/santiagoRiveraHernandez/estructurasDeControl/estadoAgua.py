print("Este programa le dirá el estado físico del agua\n")
t = float(input("Ingrese la temperatura del agua en celcius: "))
if t <= 0:
    print("A nivel del mar, el agua está en estado sólido, es hielo")
elif 0 < t < 100:
    print("A nivel del mar, el agua está en estado líquido")
else:
    print("A nivel del mar, el agua está en estado gaseoso, es vapor")