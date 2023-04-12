valor_compra = int(input("dijite el valor de la compra: "))
cantidad = int(input("dijite el cantidad de camisas: "))





descuento1 =  valor_compra * 20 /100
descuento2 = ( valor_compra * 10 )/100
valor1 = valor_compra - descuento1
valor2 = valor_compra - descuento2


if  (cantidad > 3):
    print (" tu compra es mayor de 3 camisas valor de tu compra: ", valor1, " valor total de descuento ", descuento1)
else:
    if (cantidad < 4):
        print (" tu compra es menor de 3 camisas valor de tu compra: ", valor2, " valor total de descuento ", descuento2)

    print (" gracias por su compra ")
    