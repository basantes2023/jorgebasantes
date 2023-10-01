# Creando un nuevo archivo llamado my_notes.txt
archivo = open("my_notes.txt", "w")

# Escribiendo al menos tres líneas de notas personales en el archivo
archivo.write("Primera línea de notas\n")
archivo.write("Segunda línea de notas\n")
archivo.write("Tercera línea de notas\n")

# Cerrar el archivo después de realizar las operaciones de escritura
archivo.close()

# Abrir el archivo my_notes.txt
archivo = open("my_notes.txt", "r")

# Leer el contenido del archivo línea por línea utilizando readline()
linea1 = archivo.readline()
linea2 = archivo.readline()
linea3 = archivo.readline()

# Mostrar en la consola cada línea leída
print(linea1)
print(linea2)
print(linea3)

# Cerrar el archivo después de realizar las operaciones de lectura
archivo.close()