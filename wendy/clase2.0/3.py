nombre = str(input(" digite su nombre completo "))

nota = int(input(" digite la nota "))

valorc = int(input(" valor de la colegiatura "))


descuento = ( valorc * 30 )/100
IVA = ( valorc * 10 )/100
destotal = valorc - descuento
IVAT = valorc + IVA



if nota >= 9: 
    print (" tu nota es mayor de 9 tu nota es de ", nota)

    print (" valor de la colegiatura ", valorc)

    print (" total de descuento ", descuento)

    print (" total a pagar de la colegiatura ", destotal)
else:
    print (" tu nota es menor de 9 tu nota es de ", nota)

    print (" valor de la colegiatura ", valorc)

    print (" total de IVA ", IVA)

    print (" total a pagar de conlegiatura ", IVAT)