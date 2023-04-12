def verificar_aprobacion(nota1, nota2, nota3):
        promedio = (nota1 + nota2 + nota3) / 3
        if promedio > 35:
            return "su promedio es mayor a 35 paso"
        else:
         return "su promedio es menor a 35 perdió"

resultado = verificar_aprobacion(50, 60, 70)
print(resultado) 