#input
cliente=input("Nombre y Apellidos:")
marca_polo=input("Ingrese nombre de la marca de polo:")
marca_pantalon=input("Ingrese nombre de la marca del pantalon:")
precio_polo=float(input("Ingrese precio del polo:"))
precio_pantalon=float(input("Ingrese precio pantalon:"))

#procesing
#Calcular el total a pagar
total_pagar=(precio_polo+precio_pantalon)

#output
print("#########################")
print("#  Boutique: Royal")
print("Cliente:", cliente)
print("Poloo:", marca_polo ,"                   Precio:", precio_polo)
print("Libro:", marca_pantalon ,"                Precio:", precio_pantalon)

print("Total a pagar:", total_pagar)
