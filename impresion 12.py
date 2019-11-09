#input
cliente=input("Nombre y Apellidos:")
nro_asiento=int(input("Nro de asiento:"))
nro_dni=int(input("Nro de DNI:"))
costo_pasaje=float(input("Costo del Pasaje:"))
fecha=input("Fecha de viaje:")
hora=input("Hora de viaje:")
ruta=input("Ruta de Viaje:")
igv=0.18

#Procesing
total_pagar=(costo_pasaje+(costo_pasaje*igv))


#output
print("# Empresa de Transporte: Turela" )
print("Cliente:", cliente)
print("Asiento:", nro_asiento)
print("Nro de DNI:", nro_dni)
print("Costo del pasaje", costo_pasaje)
print("Fecha:",fecha , "       Hora de salida:",hora)
print("Ruta:", ruta)
print("Total a pagar", total_pagar)
