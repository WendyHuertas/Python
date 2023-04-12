def calcular_intereses(capital, tasa_interes):
    interes = capital * tasa_interes
    if interes > 7000:
        capital += interes
    return capital
capital_i = 100000
tasa_i = 0.05

capital_F = calcular_intereses(capital_i, tasa_i)
print("capital final es: ", capital_F)

capital_F = calcular_intereses(capital_i,tasa_i)
while capital_F > calcular_intereses(capital_F,tasa_i):
    capital_F = calcular_intereses(capital_F,tasa_i)

print ("capital con intereses: ", capital_F)