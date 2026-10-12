"""
Programa 7: Convierte pesos mexicanos a otras monedas usando match-case.
Nota: tasas de ejemplo; actualizarlas antes de usar para operaciones reales.
"""

# Pesos mexicanos por una unidad de moneda extranjera (tasas ilustrativas)
PESOS_POR_USD = 18.00
PESOS_POR_EUR = 19.50
PESOS_POR_THB = 0.52
PESOS_POR_JPY = 0.12
PESOS_POR_KRW = 0.013
PESOS_POR_AUD = 11.80
PESOS_POR_PEN = 4.85
PESOS_POR_CAD = 13.20
PESOS_POR_VES = 0.50
PESOS_POR_ARS = 0.018

print("Conversor de pesos mexicanos")
print("1. Dolar (USD)   2. Euro (EUR)")
print("3. Baht (THB)    4. Yen (JPY)")
print("5. Won (KRW)     6. Dolar australiano (AUD)")
print("7. Sol (PEN)     8. Dolar canadiense (CAD)")
print("9. Bolivar (VES) 10. Peso argentino (ARS)")

try:
    pesos = float(input("Cantidad en pesos mexicanos: $"))
    opcion = input("Elige una moneda (1-10): ").strip()

    if pesos < 0:
        print("La cantidad no puede ser negativa.")
    else:
        match opcion:
            case "1":
                moneda, tasa = "USD", PESOS_POR_USD
            case "2":
                moneda, tasa = "EUR", PESOS_POR_EUR
            case "3":
                moneda, tasa = "THB", PESOS_POR_THB
            case "4":
                moneda, tasa = "JPY", PESOS_POR_JPY
            case "5":
                moneda, tasa = "KRW", PESOS_POR_KRW
            case "6":
                moneda, tasa = "AUD", PESOS_POR_AUD
            case "7":
                moneda, tasa = "PEN", PESOS_POR_PEN
            case "8":
                moneda, tasa = "CAD", PESOS_POR_CAD
            case "9":
                moneda, tasa = "VES", PESOS_POR_VES
            case "10":
                moneda, tasa = "ARS", PESOS_POR_ARS
            case _:
                moneda, tasa = None, None

        if moneda is None:
            print("Opcion no valida. Elige un numero del 1 al 10.")
        else:
            resultado = pesos / tasa
            print(f"${pesos:.2f} MXN = {resultado:.2f} {moneda}")
            print("Aviso: se usaron tasas ilustrativas, no cotizaciones en tiempo real.")
except ValueError:
    print("Entrada no valida. Escribe una cantidad numerica.")
