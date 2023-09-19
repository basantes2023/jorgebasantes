def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamada a la función con solo el monto total de la compra
monto_total1 = 5000
descuento1 = calcular_descuento(monto_total1)
monto_final1 = monto_total1 - descuento1
print(f"Monto total de la compra: ${monto_total1}")
print(f"Descuento aplicado: $ {descuento1}")
print(f"Monto final a pagar después del descuento: $ {monto_final1}")

# Llamada a la función con el monto total de la compra y el porcentaje de descuento
monto_total2 = 5000
porcentaje_descuento2 = 10
descuento2 = calcular_descuento(monto_total2, porcentaje_descuento2)
monto_final2 = monto_total2 - descuento2
print("\nLlamada con monto total de la compra y porcentaje de descuento:")
print(f"\nMonto total de la compra: $ {monto_total2}")
print(f"Porcentaje de descuento:  {porcentaje_descuento2}%")
print(f"Descuento aplicado: $ {descuento2}")
print(f"Monto final a pagar después del descuento: $ {monto_final2}")
