# pedir datos para grabar las matrices
matriz1 = []
matriz2 = []
for i in range(5):
    num = int(input("Introduce un número para la matriz 1: "))
    matriz1.append(num)
    num = int(input("Introduce un número para la matriz 2: "))
    matriz2.append(num)

# sumar el tercer elemento de cada matriz
suma = matriz1[2] + matriz2[2]

# mostrar el resultado
print("La suma del tercer elemento de ambas matrices es:", suma)
