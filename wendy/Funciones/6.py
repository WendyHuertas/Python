def suma_pares_e_impares(num):

    sumpar=0
    sumaimpar=0
    for i in num:

        if i %2==0:
            sumpar+=i
    else:
            sumaimpar+=i
    
    return sumpar, sumaimpar

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sumpar, sumaipar = suma_pares_e_impares(numeros)
print("La suma de los números pares es:", sumpar)
print("La suma de los números impares es:", sumaipar)
