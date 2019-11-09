#Calculadora_nro_13
#Esta calculadora realiza el calculo del peso

#Declaracion de variables
masa,gravedad,peso=0.0,0.0,0.0

#Calculadora
masa= 10
gravedad= 10
peso= (masa*gravedad)

#mostrar datos
print("masa =", str(masa))
print("gravedad =", str(gravedad))
print("peso =", str(peso))


#Verificadores
supera_peso_limite = (peso > 80)
print("supera peso limite?" , supera_peso_limite)
