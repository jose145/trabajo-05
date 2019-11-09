#Calculadora_nro_18
#Esta calculadora realiza el calculo de area lateral de un cono

#Declaracion de variables
valor_de_pi,radio_de_base,generatriz,area_lateral=0.0,0.0,0.0,0.0

#Calculadora
valor_de_pi= 3.1416
radio_de_base= 4
generatriz= 5
area_lateral= (valor_de_pi*radio_de_base*generatriz)

#mostrar datos
print("valor de pi=", str(valor_de_pi))
print("radio de base=", str(radio_de_base))
print("generatriz=", str(generatriz))
print("area_lateral=", str(area_lateral))

#Verificadores
supera_area_lateral_limite = (area_lateral > 26)
print("supera area lateral limite?" , supera_area_lateral_limite)
