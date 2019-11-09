#input
nombre_estudiante=input("Nombre del estudiante:")
grado_estudiante=input("Grado del estudiante:")
promedio_1=int(input("Ingrese 1er promedio:"))
promedio_2=int(input("Ingrese 2do promedio:"))
promedio_3=int(input("Ingrese 3er promedio:"))
promedio_4=int(input("Ingrese 4to promedio:"))


#procesing
#Calcular el promedio final de matematicas
promedio_final=((promedio_1+promedio_2+promedio_3+promedio_4)//4)

#output
print("I.E.E San Jose ")
print("Promedio final de matematicas")
print("Nombre del estudiante:", nombre_estudiante)
print("Grado del Estudiante:", grado_estudiante)
print("1er Promedio:", promedio_1)
print("2do Promedio:", promedio_2)
print("3er Promedio:", promedio_3)
print("4to Promedio:", promedio_4)
print("Promedio Final:", promedio_final)
