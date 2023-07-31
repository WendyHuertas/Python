#1. Encuentra el error en la siguiente línea de código. Luego tendrás que crear una excepción para evitar que el programa se caiga. Además, debes explicarle al usuario que fue lo que sucedió y darle la solución. • valor = 10/0

#El error en la línea de código es que está intentando realizar una división entre cero (10/0). En Python dividir un número entre cero es una operación indefinida y arroja una excepción llamada "ZeroDivisionError". Esta excepción se produce cuando intentas realizar una división en la que el divisor es cero.


#Para evitar que el programa se caiga y manejar esta excepción, puedes utilizar un bloque try-except. De esta manera, puedes capturar la excepción "ZeroDivisionError" y proporcionar un mensaje adecuado al usuario.

try:
    valor = 10/0
except ZeroDivisionError:
    print("Error: No es posible dividir un número entre cero.")
#El bloque try-except permite que el programa continúe su ejecución incluso si ocurre un error y, en su lugar, maneja la excepción de manera controlada, mostrando mensajes de error adecuados al usuario.



#1. Encuentra el error en la siguiente línea de código. Luego tendrás que crear una excepción para evitar que el programa se caiga. Además, debes explicarle al usuario que fue lo que sucedió y darle la solución.

#• miLista = [1,2,3,4,5 ]

#• miLista [7]

#El error en la línea de código es que está intentando acceder a un índice que está fuera del rango de la lista. En Python los índices de las listas comienzan en 0 y van hasta (longitud de la lista - 1). En este caso, la lista "miLista" tiene 5 elementos, por lo que el índice válido más alto que puedes usar es 4 (ya que el índice 0 representa el primer elemento).

#Al intentar acceder al índice 7 (miLista[7]), estarás intentando acceder a un elemento que no existe en la lista y esto generará una excepción llamada "IndexError".


#Para evitar que el programa se caiga y manejar esta excepción, puedes utilizar un bloque try-except. De esta manera, puedes capturar la excepción "IndexError" y proporcionar un mensaje adecuado al usuario.
miLista = [1, 2, 3, 4, 5]

try:
    valor = miLista[7]
except IndexError:
    print("Error: El índice está fuera del rango de la lista.")
