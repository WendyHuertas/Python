def imprimir_ipares(numeros):
    for numero in numeros:
        if numero % 2 ==1:
            print(numero)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
imprimir_ipares(numeros)