#Calculadora_nro_7
#Esta calculadora realiza el calculo de la energia

#Declaracion de variables
energia,masa,velocidad_de_luz=0.0,0.0,0.0

#Calculadora
masa= 10
velocidad_de_luz= 300000000
energia= (masa*velocidad_de_luz*velocidad_de_luz)

#mostrar datos
print("masa =", str(masa))
print("velocidad de luz =", str(velocidad_de_luz))
print("energia =", str(energia))

#Verificadores
supera_energia_limite = (energia > 200)
print("supera energia limite?" , supera_energia_limite)

