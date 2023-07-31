#1. Escriba un programa que lea dos números por teclado y determine con un valor booleano de True o False estos ejemplos:
# Leer los dos números ingresados por el usuario
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
#• Si los dos números son iguales
iguales = numero1 == numero2
#• Si los dos números son diferentes
diferentes = numero1 != numero2
#• Si el primero es mayor que el segundo
primeroEsMayor = numero1 > numero2
#• Si el segundo es mayor o igual que el primero
MayorIgual = numero2 >= numero1

# Mostrar los resultados
print("¿Los dos números son iguales?", iguales)
print("¿Los dos números son diferentes?", diferentes)
print("¿El primero es mayor que el segundo?", primeroEsMayor)
print("¿El segundo es mayor o igual que el primero?", MayorIgual)


#Conociendo los operadores lógicos, realice una comprobación si una cadena de texto ingresada desde teclado por le usuario tiene la longitud mayor o igual que 4 y a su vez que 7 (determinar con un valor booleano True o False)
# Leer la cadena de texto ingresada por el usuario
texto = input("Ingresa una cadena de texto: ")

# Obtener la longitud de la cadena de texto
longitud = len(texto)

# Comprobar si la longitud es mayor o igual que 4 y mayor o igual que 7
cumpleCondiciones = longitud >= 4 and longitud >= 7

# Mostrar el resultado como un valor booleano True o False
print("¿La longitud es mayor o igual que 4 y mayor o igual que 7?", cumpleCondiciones)
