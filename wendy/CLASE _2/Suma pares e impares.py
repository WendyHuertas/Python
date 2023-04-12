W= int (input("Ingrese la cantidad de números que desaea dijitar"))
N=0
pares = 0
impares = 0 
sumaPares = 0
sumaImpares = 0

while N<W:
    num = int(input("ingrese un número "))

    if num %2==0:
        
        pares +=1 
        sumaPares += num
    else: 
        sumaImpares+= num
        impares+= 1 
    N += 1

    


print ("Número total de números pares", pares)
print ("Número total de números impares", impares)
print ("Suma de números pares",sumaImpares+sumaPares)

 


          
    
