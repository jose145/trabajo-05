#Calculadora_nro_8
#Esta calculadora realiza el calculo de la distancia

#Declaracion de variables
velocidad,tiempo,distancia=0.0,0.0,0.0

#Calculadora
velocidad= 8
tiempo= 4
distancia= (velocidad*tiempo)

#mostrar datos
print("velocidad =", str(velocidad))
print("tiempo =", str(tiempo))
print("distancia =", str(distancia))

#Verificadores
supera_distancia_limite = (distancia > 20)
print("supera distancia limite?" , supera_distancia_limite)
