compra = float(input("Digite el valor de su compra: "))
camisas = float (input (" Digita la cantidad de camisas: "))

desc1 = (compra * 20)/100
desc2 = ( compra * 10)/100
valor1 = ( compra - desc1)
valor2 = ( compra- desc2 )/100

if (camisas > 3):
    print ("Tu compra es mayor a 3 camisa, aplica descuento de 20%")
    print ( " EL valor de su descuento es ", desc1)
    print ("El valor de su compra es: ", valor1)

else: 
    print ("Tu compra es menor de 3 camisas, aplica descuento de 10%")
    print ( " El valor del descuento fue ", desc2)
    print ("El valor de su compra es: ", valor2)