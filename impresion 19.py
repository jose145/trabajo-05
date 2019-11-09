#input
velocidad_inicial=float(input("Ingrese la Velocidad incial:"))
tiempo_segundos=float(input("Ingrese el tiempo:"))
aceleracion=float(input("Ingrese la aceleracion:"))


#Procesing
distancia=((velocidad_inicial*tiempo_segundos)+((aceleracion*tiempo_segundos+tiempo_segundos)//2))

#output
print("# Formula de la distancia")
print("Velocidad inicial:", velocidad_inicial)
print("Tiempo:", tiempo_segundos)
print("Aceleracion:", aceleracion)
print("Distancia", distancia)
