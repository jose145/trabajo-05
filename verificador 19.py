#Calculadora_nro_19
#Esta calculadora realiza el calculo de volumen de prisma

#Declaracion de variables
volumen_prisma,area_de_base_prisma,altura_prisma=0.0,0.0,0.0

#Calculadora
area_de_base_prisma= 16
altura_prisma= 8
volumen_prisma= (area_de_base_prisma*altura_prisma)

#mostrar datos
print("area de base prisma=", str(area_de_base_prisma))
print("altura prisma=", str(altura_prisma))
print("volumen prisma=", str(volumen_prisma))

#Verificadores
supera_volumen_prisma_limite = (volumen_prisma > 70)
print("supera volumen prisma limite?" , supera_volumen_prisma_limite)
