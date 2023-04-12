num1= int(input("ingrese el primer número"))
num2= int (input("Ingrese el segundo número"))

Sumapares= 0
Sumaimpares= 0

for num in range(num1, num2):
    if num %2 == 0:
     
        Sumapares += num
    else:
        if num %1 == 0:

            Sumaimpares += num
        

print ("la suma de los número pares",Sumapares)
print ("La suma de los numeros impares es", Sumaimpares)
print ("La diferencia entre la suma de los pares e impares es", abs(Sumapares-Sumaimpares))