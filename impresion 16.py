#input
carga01 =float(input("Ingrese Carga 1 :"))
carga02 =float(input("Ingrese Carga 2:"))
constante_electrica = 9000000000
distancia =float(input("Ingrese distancia:"))

#procesing
fuerza_electrica= (carga01*carga02 * constante_electrica) // (distancia*distancia)

#output
print("#Calculadora de Fuerza Electrica")
print ( " carga01 = " , carga01)
print ( " carga02 = " , carga02)
print ( " contante_electrica = " , constante_electrica)
print ( " distancia = " , distancia)
print ( " fuerza_electrica = " , fuerza_electrica)
