#Calculadora_nro_5
#Esta calculadora realiza el calculo del area del circulo

#Declaracion de variables
valor_de_pi,radio,area_del_circulo=0.0,0.0,0.0

#Calculadora
valor_de_pi= 3.1416
radio= 5
area_del_circulo= (valor_de_pi*radio*radio)

#mostrar datos
print("vaor de pi =", str(valor_de_pi))
print("radio =", str(radio))
print("area del circulo =", str(area_del_circulo))

#Verificadores
supera_area_limite = (area_del_circulo > 80)
print("supera area limite?" , supera_area_limite)
