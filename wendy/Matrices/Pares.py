# Inicializar la matriz vacía
matriz = []

# Generar los números pares menores a 20 y agregarlos a la matriz
for i in range(2, 20, 2):
    fila = [i, i+2, i+4, i+6]
    matriz.append(fila)

# Mostrar el contenido de la matriz
for fila in matriz:
    print(fila)
 