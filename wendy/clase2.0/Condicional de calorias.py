activ = float(input("Escriba 1 si estuvo dormido o 2 si estava sentado : "))
tiempo = float(input("ingrese el tiempo en minutos que estuvo haciendo esta actividad  "))
CDormir = 1.08
CSentado = 1.66

caloriasS = tiempo * 1.66
caloriasD = tiempo * 1.08 

if (activ == "1" ):
 
    print ("El paciemte consume: ", caloriasD, "calorias en total.")

else:
    
    print ("El paciente comsume :", caloriasS, "calorias en total,")
