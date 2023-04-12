ventras_mayoresa500 = 0
ventas_entre_200_550 = 0
total_ventas = 0
total_entre = 0
ventas_mayores_lista = []
ventas_entre = []
promedio_entre_200_550 = 0
promedio_mayores_550 = 0

for i in range(15):
    precio = float(input("ingrese el precio de la venta: " + str(i+1) + ": "))

    if precio > 550:
        ventras_mayoresa500 += 1
        total_ventas += precio
        ventas_mayores_lista.append(precio)
    
    elif precio > 200 and precio <= 550:
        ventas_entre_200_550 += 1
        total_entre += precio
        ventas_entre.append(precio)

promedio_mayores_550 = total_ventas/len(ventas_mayores_lista)
promedio_entre_200_550 =total_entre /len(ventas_entre)


print ("VENTAS")
print("1. Número de ventas mayores a 550:", ventas_mayores_lista)
print("2. Número de ventas entre 200 y 550:", ventas_entre_200_550)
print("3. Promedio de ventas mayores a 550:", promedio_mayores_550)
print("3.Promedio de ventas entre 200 y 550:", promedio_entre_200_550)
print("4. Ventas mayores a 550:", ventas_mayores_lista)
print("5. Ventas entre 200 y 550:", ventas_entre_200_550)
