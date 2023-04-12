nota1 = int(input("Digite la primera nota parcial "))
nota2 = int(input("Digite la segunda nota parcial "))
nota3 = int(input("Digite la tercera nota parcial "))
examen = int(input("Digite la nota de su examen final "))
trabajo = int(input("Digite la nota de su trabajo final "))
porcent_notas = ((nota1 + nota2 + nota3)/3)*0.55
examen = examen * 0.30
trabajo = trabajo * 0.15
print ("Calificacion final para Algoritmos es ",porcent_notas + examen + trabajo)