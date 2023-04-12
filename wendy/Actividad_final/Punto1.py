x = input("Ingrese el valor de X: ")
y = input("Ingrese el valor de Y: ")


x = int(x)
y = int(y)
if x > 0 and y > 0:
 print("esta en cuadrante I ")
elif x < 0 and y > 0:
     print("esta en cuadrante II ")
elif x < 0 and y < 0:
     print(" esta en cuadrante III ")
elif x > 0 and y < 0:
    print("esta en cuadrante IV ")

