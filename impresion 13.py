#input
nombre_alumno=input("Nombre del alumno:")
grado_estudiante=input("Grado del alumno: ")
nota01=int(input("Ingrese 1era nota:"))
nota02=int(input("Ingrese 2da nota:"))
nota03=int(input("Ingrese 3era nota:"))

#procesing
promedio=((nota01+nota02+nota03)//3)

#output
print("I.E. Virgen de Fatima ")
print("Promedio de notas de semestre")
print("Nombre del alumno:", nombre_alumno)
print("Grado del Estudiante:", grado_estudiante)
print("Nota Nº1:",nota01)
print("Nota Nº2:", nota02)
print("Nota Nº3:", nota03)
print("Nota Final:", promedio)
