#imprima números y sumelos 
notas1=[]
notas2= float(input("Ingrese las notas y escriba 99 para terminar"))


while notas2 !=99:

    if notas2 >=0:
        notas1. append(notas2)
        notas2= int (input("Ingrse las notas y escriba 99 para terminar"))
    else:
        print("La debe ser un entero positivo.")

if len(notas1) >0:
    promedio = sum(notas1) / len(notas1)
    print ("El promedio de las notas es:", promedio)
else:
    print("No  hay notas ingresadas") 

