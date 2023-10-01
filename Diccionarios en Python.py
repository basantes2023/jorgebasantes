# Crear un diccionario con información personal ficticia
informacion_personal = {
    "Nombre": "Luis Flores",
    "Edad": 44,
    "Ciudad": "Quito",
    "Profesion": "Ingeniero"
}

# Acceder al valor de la clave "Ciudad" y modificarlo
informacion_personal["Ciudad"] = "Ibarra"

# Agregar una nueva clave-valor para "profesion"
informacion_personal["Profesion"] = "Mecanico"

# Verificar si la clave "Telefono" existe y agregarlo si no esxiste
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "0984025075"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["Edad"]

# Imprimir el diccionario final
print(informacion_personal)