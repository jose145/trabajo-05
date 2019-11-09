#input
cliente=input("Nombre del Cliente:")
fruta=input("Tipo de fruta:")
cantidad=float(input ("Cantidad:"))
precio_kg=float(input("Ingrese el precio:"))
total=(cantidad*precio_kg)

#output
print("Compra de Fruta")
print("Cliente:" , cliente)
print("Fruta", fruta)
print("Cantidad: ", cantidad, "Kg")
print("Precio por Kg:", precio_kg)
print("Total a pagar:", total)
