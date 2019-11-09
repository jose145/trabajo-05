#Calculadora_nro_6
#Esta calculadora realiza el calculo del area del triangulo

#Declaracion de variables
base_del_triangulo,altura_del_triangulo,area_del_triangulo=0.0,0.0,0.0

#Calculadora
base_del_triangulo= 5
altura_del_triangulo= 8
area_del_triangulo= (base_del_triangulo*altura_del_triangulo)/2

#mostrar datos
print("base del triangulo =", str(base_del_triangulo))
print("altura_del_triangulo =", str(altura_del_triangulo))
print("area del triangulo =", str(area_del_triangulo))

#Verificadores
supera_area_limite = (area_del_triangulo > 84)
print("supera area limite?" , supera_area_limite)
