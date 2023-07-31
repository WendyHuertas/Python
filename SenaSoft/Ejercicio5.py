#1. Escriba una función que muestre por consola un saludo personalizado. Por ejemplo ‘¡Hola mundo!’
def saludar(nombre):
    print(f'¡Hola {nombre}!')

# Ejemplo de uso de la función
nombreUsuario = input("Ingresa tu nombre: ")
saludar(nombreUsuario)


#1. Escriba una función que reciba un nombre por parámetro y que luego muestre en pantalla ¡Hola <nombre>!
def saludar(nombre):
    print(f'¡Hola {nombre}!')

# Ejemplo de uso de la función
nombre_usuario = input("Ingresa tu nombre: ")
saludar(nombre_usuario)


#1. Cree una función que le pida el usuario su nombre y su edad, luego muestre en pantalla los resultados.

def obtenerNombreEdad():
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")

    return nombre, edad

# Llamada a la función y obtención de los resultados
nombre_usuario, edad_usuario = obtenerNombreEdad()

# Mostrar los resultados en pantalla
print(f"Tu nombre es: {nombre_usuario}")
print(f"Tienes {edad_usuario} años.")


#1. Definir una función que reciba dos números por parámetros y que luego los sume.
def sumar_numeros(num1, num2):
    suma = num1 + num2
    return suma

# Ejemplo de uso de la función
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

resultado = sumar_numeros(numero1, numero2)
print(f"El resultado de la suma es: {resultado}")

