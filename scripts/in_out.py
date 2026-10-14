"""En este programa se ilustra el uso de la lectura y la escritura de ficheros"""

archivo_entrada='masavolumen.txt'
archivo_salida='masavolumendensidad.txt'

#abrimos los archivos
with open(archivo_entrada, 'r') as f_in, open(archivo_salida, 'w') as f_out:
    # 1. Leer y escribir el encabezado
    encabezado = f_in.readline()
    f_out.write(f"{encabezado.strip()}   Densidad (g/m^3)\n")
    
    # 2. Procesar linea a linea
    for linea in f_in:
        partes = linea.split()
        if partes:  # Omite lineas vacias
            masa = float(partes[0])
            volumen = float(partes[1])
            densidad = masa / volumen
            
            # 3. Guardar resultados 
            f_out.write(f"{masa:<10.1f} {volumen:<10.2f} {densidad:<12.2f}\n")