#Calculadora_nro_20
#Esta calculadora realiza el calculo de volumen de cilindro

#Declaracion de variables
volumen_cilindro,radio_de_base_cilindro,altura_cilindro,valor_pi=0.0,0.0,0.0,0.0

#Calculadora
radio_de_base_cilindro= 5
altura_cilindro= 9
valor_pi= 3.1416
volumen_cilindro= (radio_de_base_cilindro*radio_de_base_cilindro*altura_cilindro*valor_pi)

#mostrar datos
print("radio de base cilindro=", str(radio_de_base_cilindro))
print("altura cilindro=", str(altura_cilindro))
print("valor pi=", str(valor_pi))
print("volumen_cilindro=", str(volumen_cilindro))


#Verificadores
supera_volumen_cilindro_limite = (volumen_cilindro > 20)
print("supera volumen cilindro limite?" , supera_volumen_cilindro_limite)
