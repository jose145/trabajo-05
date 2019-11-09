#Calculadora_nro_1
#Esta calculadora realiza el calculo del area del rombo

#Declaracion de variables
diagonal_menor,diagonal_mayor,area_del_rombo=0.0,0.0,0.0

#Calculadora
diagonal_menor= 5
diagonal_mayor= 10
area_del_rombo= (diagonal_menor*diagonal_mayor)/2

#mostrar datos
print("diagonal menor =", str(diagonal_menor))
print("diagonal mayor =", str(diagonal_mayor))
print("area del rombo =", str(area_del_rombo))


#Verificadores
supera_area_limite = (area_del_rombo > 20)
print("supera area limite?" , supera_area_limite)
