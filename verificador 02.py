#Calculadora_nro_2
#Esta calculadora realiza el calculo del area del paralelogramo

#Declaracion de variables
base_del_paralelogramo,altura_del_paralelogramo,area_del_paralelogramo=0.0,0.0,0.0

#Calculadora
base_del_paralelogramo= 8
altura_del_paralelogramo= 6
area_del_paralelogramo= (base_del_paralelogramo*altura_del_paralelogramo)

#mostrar datos
print("base del paralelogramo =", str(base_del_paralelogramo))
print("altura del paralelogramo =", str(altura_del_paralelogramo))
print("area del paralelogramo =", str(area_del_paralelogramo))


#Verificadores
supera_area_limite = (area_del_paralelogramo > 15)
print("supera area limite?" , supera_area_limite)


