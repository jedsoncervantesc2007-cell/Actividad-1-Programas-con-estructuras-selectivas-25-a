"""
Programa 4: Calcula el precio final de un producto con descuento.
"""

try:
    precio = float(input("Ingresa el precio original: $"))

    if precio < 0:
        print("El precio no puede ser negativo.")
    elif precio <= 100:
        descuento = 0
    elif precio <= 200:
        descuento = 0.10
    elif precio <= 500:
        descuento = 0.20
    else:
        descuento = 0.25

    if precio >= 0:
        ahorro = precio * descuento
        precio_final = precio - ahorro
        print(f"Descuento aplicado: {descuento:.0%}")
        print(f"Ahorro: ${ahorro:.2f}")
        print(f"Precio final: ${precio_final:.2f}")
except ValueError:
    print("Entrada no valida. Escribe un precio numerico.")
