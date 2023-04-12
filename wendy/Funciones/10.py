def minutos_a_segundos(nombre):
    minutos = int(input(" ingrese la cantidad de minutos para convertir a segundos: "))
    segundos = minutos * 60
    print(f"{minutos} minutos equivalen a {segundos} segundos ")

    minutos_restantes = 60 - minutos
    print(f"Faltan {minutos_restantes} minutos para completar una hora ")

nombre = input("Ingresa tu nombre: ")
minutos_a_segundos(nombre)
