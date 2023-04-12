nota1 = int(input("dijite la nota 1: "))
nota2 = int(input("dijite la nota 2: "))
nota3 = int(input("dijite la nota 3: "))

promedio = (nota1 + nota2 + nota3)/3

if (promedio >= 35):
    print ("su nota es mayor: ",promedio, "aprobo" )
else:
    print ("su nota es menor: ", promedio, "reprobo")