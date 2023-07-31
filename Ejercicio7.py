#1. Cree una clase Persona con sus atributos correspondientes:nombre, edad, sexo, nacionalidad. Luego cree una instancia de la clase Persona.
class Persona:
    def __init__(self, nombre, edad, sexo, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.nacionalidad = nacionalidad

# Crear una instancia de la clase Persona
persona1 = Persona(nombre="Juan", edad=30, sexo="Masculino", nacionalidad="Mexicana")

# Acceder a los atributos de la instancia y mostrarlos en consola
print("Nombre:", persona1.nombre)
print("Edad:", persona1.edad)
print("Sexo:", persona1.sexo)
print("Nacionalidad:", persona1.nacionalidad)



#1. Cree una clase Auto con sus atributos correspondientes: marca, modelo, año, color. Defina también un método, donde luego al instanciar la clase nos diga si el auto esta encendido o apagado.
class Auto:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.encendido = False

    def estado_motor(self):
        if self.encendido:
            return "El auto está encendido."
        else:
            return "El auto está apagado."

# Crear una instancia de la clase Auto
mi_auto = Auto(marca="Toyota", modelo="Corolla", año=2022, color="Rojo")

# Mostrar los atributos del auto
print("Marca:", mi_auto.marca)
print("Modelo:", mi_auto.modelo)
print("Año:", mi_auto.año)
print("Color:", mi_auto.color)

# Mostrar el estado del motor del auto
print(mi_auto.estado_motor())
