# cargar dos matrices
matriz1 = [1, 2, 3, 4, 5]
matriz2 = [6, 7, 8, 9, 10]

# sumar las dos matrices
matriz3 = []
for i in range(len(matriz1)):
    suma = matriz1[i] + matriz2[i]
    matriz3.append(suma)

# mostrar el resultado
print("La matriz resultante de la suma es:", matriz3)
