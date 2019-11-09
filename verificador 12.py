#Calculadora_nro_12
#Esta calculadora realiza el calculo de la potencia

#Declaracion de variables
trabajo,tiempo,potencia=0.0,0.0,0.0

#Calculadora
trabajo= 20
tiempo= 5
potencia= (trabajo/tiempo)

#mostrar datos
print("trabajo =", str(trabajo))
print("tiempo =", str(tiempo))
print("potencia =", str(potencia))

#Verificadores
supera_potencia_limite = (potencia > 15)
print("supera potencia limite?" , supera_potencia_limite)
