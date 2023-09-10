# Definición de la función
def calcular_temperatura_promedio(datos_temperaturas):
    temperaturas_promedio_ciudades = []

    for ciudad_temperaturas in datos_temperaturas:
        total_temperaturas = sum(ciudad_temperaturas)
        semanas = len(ciudad_temperaturas)
        temperatura_promedio = total_temperaturas / semanas
        temperaturas_promedio_ciudades.append(temperatura_promedio)

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