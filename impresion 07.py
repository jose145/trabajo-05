#input
masa=float(input("Ingrese la masa:"))
altura= float(input("ingrese la altura"))
aceleracion_gravedad=float(input("Ingrese la aceleracion:"))


#Procesing
#Calcular la formula de la Energia Potencial Gravitatoria
energia_potencial_gravitatoria=(masa*aceleracion_gravedad*altura)

#output
print("# Formula de la energia potencial gravitatoria")
print("Masa:", masa)
print("Aceleracion de la gravedad:", aceleracion_gravedad)
print("Altura:", altura)
print("Energia potencial gravitatoria", energia_potencial_gravitatoria)
