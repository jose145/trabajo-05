#Calculadora_nro_4
#Esta calculadora realiza el calculo del area del trapecio

#Declaracion de variables
base_menor,base_mayor,altura_del_trapecio=0.0,0.0,0.0

#Calculadora
base_menor= 4
base_mayor= 10
altura_del_trapecio=6
area_del_trapecio=((base_menor+base_mayor)*altura_del_trapecio)/2

#mostrar datos
print("base menor =", str(base_menor))
print("base mayor =", str(base_mayor))
print("altura del trapecio =", str(altura_del_trapecio))
print("area del trapecio =", str(area_del_trapecio))

#Verificadores
supera_area_limite = (area_del_trapecio > 60)
print("supera area limite?" , supera_area_limite)
