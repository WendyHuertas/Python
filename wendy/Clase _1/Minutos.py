# Pide nombre, minutos y dice segundos y minutos faltantes
import string


nombre= (input("escriba su nombre"))
minutos= float(input("escriba los minutos requeridos"))

segundos= minutos*60
minutos= segundos/60
minutos= 60-minutos 
print ("Su nombre ", nombre)
print ("segundos ", segundos)
print ("Minutos faltantes para completar la hora ", minutos)