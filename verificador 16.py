#Calculadora_nro_16
#Esta calculadora realiza el calculo del calor del cuerpo

#Declaracion de variables
calor_del_cuerpo,masa_del_cuerpo,calor_especifico_del_cuerpo,variacion_de_temperatura=0.0,0.0,0.0,0.0

#Calculadora
masa_del_cuerpo= 30
calor_especifico_del_cuerpo= 1
variacion_de_temperatura= 4
calor_del_cuerpo= (masa_del_cuerpo*calor_especifico_del_cuerpo*variacion_de_temperatura)

#mostrar datos
print("masa del cuerpo =", str(masa_del_cuerpo))
print("calor especifico del cuerpo =", str(calor_especifico_del_cuerpo))
print("variacion_de_temperatura =", str(variacion_de_temperatura))
print("calor del cuerpo =", str(calor_del_cuerpo))

#Verificadores
supera_calor_del_cuerpo_limite = (calor_del_cuerpo > 40)
print("supera calor del cuerpo limite?" , supera_calor_del_cuerpo_limite)
