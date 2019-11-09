#input
cliente=input("Nombre y Apellidos:")
nro_dni=int(input("Ingrese numero de DNI:"))
nro_ruc=int(input("Ingese numero de ruc:"))
nombre_libro1=input("Ingrese nombre del 1er libro:")
nombre_libro2=input("Ingrese nombre del 2do libro:")
precio_libro1=float(input("Ingrese Importe del 1ero libro:"))
precio_libro2=float(input("Ingrese Importe del 2do libro:"))

#procesing
total_pagar=(precio_libro1+precio_libro2)

#output
print("#########################")
print("#  Libreria Bazar: El Diamante")
print("Cliente:", cliente)
print("Nro de DNI:", nro_dni)
print("Nro de Ruc:",nro_ruc)
print("Libro:", nombre_libro1 ,"                   Precio:", precio_libro1)
print("Libro:", nombre_libro2 ,"                Precio:", precio_libro2)

print("Total a pagar:", total_pagar)
