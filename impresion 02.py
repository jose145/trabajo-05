#input
cliente=input("Nombre y Apellidos:")
costo_encargo=float(input("Costo del encargo:"))
fecha=input("Fecha de entrega:")
hora=input("Hora de partida:")
recorrido=input("Recorrido del encargo:")
igv=0.18

#procesing
#Calcular el total a pagar
total_pagar=(costo_encargo+(costo_encargo*igv))

#output
print("# Empresa de Encomiendas: Serex" )
print("Cliente:", cliente)
print("Costo del encargo", costo_encargo)
print("Fecha de entrega :",fecha , "       Hora de partida:",hora)
print("Recorrido:", recorrido)
print("Total a pagar", total_pagar)
