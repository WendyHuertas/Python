#1. Escriba un programa que almacene la cadena de caracteres contraseña en una variable, para luego preguntarle al usuario por la contraseña. Luego, imprima en la consola si la contraseña que el usuario ingreso coincide con la guardada en variable.

# Almacenar la contraseña en una variable
contraseñaGuardada = "contraseña"

# Pedir al usuario que ingrese la contraseña
contraseñaIngresada = input("Ingresa la contraseña: ")

# Comparar la contraseña ingresada con la guardada y mostrar el resultado
if contraseñaIngresada == contraseñaGuardada:
    print("¡Contraseña correcta!")
else:
    print("¡Contraseña incorrecta!")

#1. Realice un programa que le pida al usuario dos números y muestre por consola su división. Si el divisor es cero el programa debe mostrar un error.
# Pedir al usuario que ingrese los dos números
dividendo = float(input("Ingresa el dividendo: "))
divisor = float(input("Ingresa el divisor: "))

# Verificar si el divisor es cero
if divisor == 0:
    print("Error: El divisor no puede ser cero.")
else:
    # Realizar la división y mostrar el resultado
    resultado = dividendo / divisor
    print("El resultado de la división es:", resultado)


#1. Escriba un programa que le pida al usuario por teclado un numero entero y muestre en consola si es par o impar.

# Pedir al usuario que ingrese un número entero
numero = int(input("Ingresa un número entero: "))

# Verificar si el número es par o impar y mostrar el resultado
if numero % 2 == 0:
    print("El número ingresado es par.")
else:
    print("El número ingresado es impar.")

#1. Escriba un programa donde se evalué el ingreso a menores de edad, si la persona tiene menos de 19 años el programa le debe mostrar en pantalla que ¡No puede ingresar!, de caso contrario que le diga ¡Bienvenido!

# Pedir al usuario que ingrese su edad
edad = int(input("Ingresa tu edad: "))

# Verificar si es menor de 19 años y mostrar el mensaje correspondiente
if edad < 19:
    print("¡No puedes ingresar!")
else:
    print("¡Bienvenido!")