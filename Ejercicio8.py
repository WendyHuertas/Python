#1. Cree una clase Persona con sus atributos correspondientes. Luego cree una clase Empleado que herede esos atributos de la clase Padre.
class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

class Empleado(Persona):
    def __init__(self, nombre, edad, sexo, cargo, salario):
        super().__init__(nombre, edad, sexo)
        self.cargo = cargo
        self.salario = salario

# Crear una instancia de la clase Persona
persona1 = Persona(nombre="Juan", edad=30, sexo="Masculino")

# Crear una instancia de la clase Empleado
empleado1 = Empleado(nombre="María", edad=25, sexo="Femenino", cargo="Analista", salario=45000)

# Mostrar los atributos de la persona
print("Persona:")
print("Nombre:", persona1.nombre)
print("Edad:", persona1.edad)
print("Sexo:", persona1.sexo)

# Mostrar los atributos del empleado
print("\nEmpleado:")
print("Nombre:", empleado1.nombre)
print("Edad:", empleado1.edad)
print("Sexo:", empleado1.sexo)
print("Cargo:", empleado1.cargo)
print("Salario:", empleado1.salario)



#1. Realice una clase persona, luego haga una clase empleado que herede los atributos de la clase Persona. Por último, cree un método de la clase empleado e instancie la clase.
class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

class Empleado(Persona):
    def __init__(self, nombre, edad, sexo, cargo, salario):
        super().__init__(nombre, edad, sexo)
        self.cargo = cargo
        self.salario = salario

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")
        print(f"Cargo: {self.cargo}")
        print(f"Salario: {self.salario}")

# Crear una instancia de la clase Empleado
empleado1 = Empleado(nombre="María", edad=25, sexo="Femenino", cargo="Analista", salario=45000)

# Mostrar la información del empleado
empleado1.mostrar_informacion()
