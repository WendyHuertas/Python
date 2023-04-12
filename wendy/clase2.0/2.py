capital = int(input("escriba el valor del capital prestado: "))



if  capital <50000:
    interes = capital * 0.03
    print ("se aplico un 3%_de interes ")
else:
    interes = capital * 0.02
    print  ("se aplico un 2%_de interes ")



print ("el interes a pagar es $", interes)

print ("la cuota total a pagar es $", capital + interes)