#input
diagonal_mayor=float(input("Diagonal Mayor:"))
diagonal_menor=float(input("Diagonal Menor:"))
altura=float(input("Altura:"))

#procesing
area=float(((diagonal_mayor+diagonal_menor)*altura)//2)

#output
print("Area de un Rombo")
print("Diagonal Mayor:", diagonal_mayor)
print("Diagonal Menor:", diagonal_menor)
print("Altura:", altura)
print("Area:", area)
