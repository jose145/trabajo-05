#input
base_mayor=float(input("Base Mayor:"))
base_menor=float(input("Base Menor:"))
altura=float(input("Altura:"))

#procesing
#Calcular el area de un trapecio
area=float(((base_mayor+base_menor)*altura)//2)

#output
print("#Calcularemos el area de un trapecio")
print("Base Mayor:", base_mayor)
print("Base Menor:", base_menor)
print("Altura:", altura)
print("Area:", area)
