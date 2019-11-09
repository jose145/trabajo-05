#Calculadora_nro_9
#Esta calculadora realiza el calculo del trabajo

#Declaracion de variables
fuerza,distancia,trabajo=0.0,0.0,0.0

#Calculadora
distancia= 20
fuerza= 15
trabajo= (distancia*fuerza)

#mostrar datos
print("distancia =", str(distancia))
print("fuerza =", str(fuerza))
print("trabajo =", str(trabajo))

#Verificadores
supera_trabajo_limite = (trabajo > 150)
print("supera trabajo limite?" , supera_trabajo_limite)
