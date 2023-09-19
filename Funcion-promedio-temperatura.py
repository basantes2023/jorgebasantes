# Definición de la función
def calcular_temperatura_promedio(datos_temperaturas):
    # Crear una lista para almacenar las temperaturas promedio de cada ciudad.
    temperaturas_promedio_ciudades = []

    # Iterar a través de las temperaturas de cada ciudad.
    for ciudad_temperaturas in datos_temperaturas:
        # Calcular la suma de todas las temperaturas de la ciudad.
        total_temperaturas = sum(ciudad_temperaturas)
        # Obtiene el número de semanas, la lista de temperaturas.
        semanas = len(ciudad_temperaturas)
        # Calcular el promedio de temperatura dividiendo la suma total por el número de semanas.
        temperatura_promedio = total_temperaturas / semanas
        # Agregar el promedio a la lista de temperaturas promedio de ciudades.
        temperaturas_promedio_ciudades.append(temperatura_promedio)

    # Devolver la lista de temperaturas promedio de cada ciudad.
    return temperaturas_promedio_ciudades

# Datos de temperaturas
datos_temperaturas = [
    [29, 30, 24, 22],  # Temperaturas de la primera ciudad durante 4 semanas.
    [25, 26, 20, 30],  # Temperaturas de la segunda ciudad durante 4 semanas.
    [28, 31, 23, 27]   # Temperaturas de la tercera ciudad durante 4 semanas.
]

# Llamada a la función para calcular las temperaturas promedio
promedios = calcular_temperatura_promedio(datos_temperaturas)

# Mostrar los resultados
for i, promedio in enumerate(promedios):
    print(f"Promedio de temperatura en la ciudad {i+1}: {promedio}°C")