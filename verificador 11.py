#Calculadora_nro_11
#Esta calculadora realiza el calculo de la densidad

#Declaracion de variables
masa,volumen,densidad=0.0,0.0,0.0

#Calculadora
masa= 9
volumen= 27
densidad= (masa/volumen)

#mostrar datos
print("masa =", str(masa))
print("volumen =", str(volumen))
print("densidad =", str(densidad))

#Verificadores
supera_densidad_limite = (densidad > 30)
print("supera densidad limite?" , supera_densidad_limite)
