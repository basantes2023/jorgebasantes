# Programa 2: Ordenación de Arreglo Multidimensional
# Definir la matriz bidimensional
matriz = [
    [6, 3, 8],
    [5, 7, 2],
    [4, 1, 9]
]

# Función para ordenar una fila de la matriz en orden ascendente utilizando QuickSort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for element in arr[1:]:
            if element < pivot:
                left.append(element)
            else:
                right.append(element)
        return quick_sort(left) + [pivot] + quick_sort(right)

# Fila que ordenamos
fila_a_ordenar = 2

# Imprimir la matriz original
print("Matriz Original:")
for fila in matriz:
    print(fila)

# Ordenar la fila seleccionada utilizando QuickSort
fila_a_ordenar = min(max(fila_a_ordenar, 0), len(matriz) - 1)
matriz[fila_a_ordenar] = quick_sort(matriz[fila_a_ordenar])

# Imprimir la matriz con la fila ordenada
print("\nMatriz con la Fila Ordenada:")
for fila in matriz:
    print(fila)