#1. Escriba un programa que almacene en una Lista los cursos que has cursado o los que te gustaría cursar en Udemy. Luego muestre la lista por consola.

# Crear una lista para almacenar los cursos
cursosUdemy = []

# Pedir al usuario que ingrese los cursos
print("Ingresa los cursos que has cursado o te gustaría cursar en Udemy. Escribe 'fin' para terminar.")
while True:
    curso = input("Curso: ")
    if curso.lower() == 'fin':
        break
    cursosUdemy.append(curso)

# Mostrar la lista de cursos por consola
print("Lista de cursos en Udemy:")
for curso in cursosUdemy:
    print(curso)


#1. Escriba un programa que almacene personas en una lista, luego que le muestre por pantalla el mensaje de ‘Su nombre es ‘nombre’
# Crear una lista para almacenar personas
personas = []

# Pedir al usuario que ingrese las personas
print("Ingresa el nombre de las personas. Escribe 'fin' para terminar.")
while True:
    nombre = input("Nombre: ")
    if nombre.lower() == 'fin':
        break
    personas.append(nombre)

# Mostrar los mensajes personalizados por consola
for nombre in personas:
    print("Su nombre es {nombre}.")

#1. Escribir un programa que guarde en una variable un diccionario con los siguientes valores {'Euro':'€', 'Dollar':'$', 'Yen':'¥'} Luego pregunte al usuario por una divisa y muestre en consola el símbolo o un mensaje de advertencia si esa divisa no se encuentra en el diccionario.

# Definir el diccionario con las divisas y sus símbolos
diccionarioDivisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

# Pedir al usuario que ingrese una divisa
divisa = input("Ingresa una divisa: ")

# Buscar la divisa en el diccionario y mostrar el símbolo o mensaje de advertencia
if divisa in diccionarioDivisas:
    simbolo = diccionarioDivisas[divisa]
    print(f"El símbolo de {divisa} es {simbolo}.")
else:
    print("Advertencia: La divisa ingresada no se encuentra en el diccionario.")


#1. En una tupla coloque los siguientes valores: números enteros, decimales, String, colecciones. Luego muestre en consola.

# Crear una tupla con diferentes tipos de datos
miTupla = (10, 3.14, "Hola", [1, 2, 3], {"nombre": "Juan", "edad": 30})

# Mostrar la tupla en consola
print(miTupla)