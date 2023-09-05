# Programa 1: Búsqueda en Arreglo Multidimensional
# Matriz bidimensional de 3x3
matriz = [
  [1,  2,  3], 
  [12, 5,  9], 
  [7,  8, 10]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):

  for fila in range(len(matriz)):
    for columna in range(len(matriz[0])):
      if matriz[fila][columna] == valor:
        return fila, columna
  return None

# Solicitar al usuario que ingrese un valor a buscar
valor_buscado = int(input("Ingrese el valor a buscar: "))

# Llamar a la función para buscar el valor
posicion = buscar_valor(matriz, valor_buscado)

# Imprimir un mensaje indicando si el valor se encontró o no
if posicion is not None:
  print(f"El valor {valor_buscado} se encontró en la posición ({posicion[0]}, {posicion[1]})")
else:
  print(f"El valor {valor_buscado} no se encontró en la matriz")



