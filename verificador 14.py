#Calculadora_nro_14
#Esta calculadora realiza el calculo de la aceleracion

#Declaracion de variables
velocidad,tiempo,aceleracion=0.0,0.0,0.0

#Calculadora
velocidad= 5
tiempo= 10
aceleracion= (velocidad/tiempo)

#mostrar datos
print("velocidad =", str(velocidad))
print("tiempo =", str(tiempo))
print("aceleracion =", str(aceleracion))

#Verificadores
supera_aceleracion_limite = (aceleracion > 8)
print("supera aceleracion limite?" , supera_aceleracion_limite)
