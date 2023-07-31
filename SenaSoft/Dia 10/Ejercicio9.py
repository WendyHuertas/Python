#Cree un modulo con todas las operaciones matemáticas, luego impórtela en un archivo.py y realice las operaciones matemáticas llamando a cada función.
# Archivo: operaciones_matematicas.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Error: No es posible dividir entre cero.")

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a >= 0:
        return a ** 0.5
    else:
        raise ValueError("Error: No es posible calcular la raíz cuadrada de un número negativo.")


