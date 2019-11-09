#Calculadora_nro_15
#Esta calculadora realiza el calculo de la energia potencial gravitatoria

#Declaracion de variables
energia_potencial_gravitatoria,masa_del_cuerpo,gravedad,altura=0.0,0.0,0.0,0.0

#Calculadora
masa_del_cuerpo= 20
gravedad= 10
altura= 15
energia_potencial_gravitatoria= (masa_del_cuerpo*gravedad*altura)

#mostrar datos
print("masa del cuerpo =", str(masa_del_cuerpo))
print("gravedad =", str(gravedad))
print("altura =", str(altura))
print("energia potencial gravitatoria =", str(energia_potencial_gravitatoria))

#Verificadores
supera_energia_potencial_gravitatoria_limite = (energia_potencial_gravitatoria > 150)
print("supera energia potencial gravitatoria limite?" , supera_energia_potencial_gravitatoria_limite)
