#Calculadora_nro_17
#Esta calculadora realiza el calculo de cantidad de movimiento

#Declaracion de variables
masa_de_cuerpo,velocidad,cantidad_de_movimiento=0.0,0.0,0.0

#Calculadora
masa_de_cuerpo= 12
velocidad= 6
cantidad_de_movimiento= (masa_de_cuerpo*velocidad)

#mostrar datos
print("velocidad =", str(velocidad))
print("masa de cuerpo =", str(masa_de_cuerpo))
print("cantidad de movimiento =", str(cantidad_de_movimiento))

#Verificadores
supera_cantidad_de_movimiento_limite = (cantidad_de_movimiento > 50)
print("supera cantidad de movimiento limite?" , supera_cantidad_de_movimiento_limite)
