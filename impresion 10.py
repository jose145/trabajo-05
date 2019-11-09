#input
velocidad_01 =float(input("Ingrese velocidad 1:"))
velocidad_02 =float(input("Ingrese velocidad 2:"))
distancia =float(input("Ingrese distancia:"))

#procesing
tiempo_encuentro= ((distancia)//(velocidad_01+velocidad_02))

#output
print("#Calcular la formula de tiempo de encuentro")
print ( " Velocidad 1 = " , velocidad_01)
print ( " Velocidad 2 = " , velocidad_02)
print ( " distancia = " , distancia)
print ( " tiempo_encuentro = " , tiempo_encuentro)
