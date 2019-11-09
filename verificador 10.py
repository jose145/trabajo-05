#Calculadora_nro_10
#Esta calculadora realiza el calculo de la presion

#Declaracion de variables
fuerza,area,presion=0.0,0.0,0.0

#Calculadora
area= 16
fuerza= 8
presion= (fuerza/area)

#mostrar datos
print("area =", str(area))
print("fuerza =", str(fuerza))
print("presion =", str(presion))

#Verificadores
supera_presion_limite = (presion > 60)
print("supera presion limite?" , supera_presion_limite)
