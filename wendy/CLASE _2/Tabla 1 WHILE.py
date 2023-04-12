print ("Tablas de multiplicar")
tabla=0
num =0
while tabla< 10+1:
    print ("tabla del",tabla)
    while num <10+1:
        print (tabla, "x", num, "=",tabla*num)
        num+=1
    tabla+=1
    num-=10
    