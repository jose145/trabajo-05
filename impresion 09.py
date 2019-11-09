#Input
comprador= input("comprador")
kg= int(input("Nro de Kg"))
Pu= float(input("precio unitario"))

#Procesing
#Calcular el precio total
precio_total= (kg*Pu)

#Output
print("########################")
print("BOLETA DE VENTA")
print("########################")
print("#")
print("#Comprador :", comprador)
print("#Item    :", kg ,  "de cebolla")
print("#P.U.    :", Pu )
print("#Total   :", precio_total)
print("########################")
