"""
Programa 6: Convierte Celsius a Fahrenheit o Kelvin con match-case.
"""

try:
    celsius = float(input("Temperatura en grados Celsius: "))
    print("Convertir a:")
    print("1. Fahrenheit")
    print("2. Kelvin")
    opcion = input("Elige una opcion (1-2): ").strip()

    match opcion:
        case "1":
            fahrenheit = (celsius * 9 / 5) + 32
            print(f"Temperatura en Fahrenheit: {fahrenheit:.2f} F")
        case "2":
            kelvin = celsius + 273.15
            if kelvin < 0:
                print("La temperatura no puede ser menor que el cero absoluto.")
            else:
                print(f"Temperatura en Kelvin: {kelvin:.2f} K")
        case _:
            print("Opcion no valida. Elige 1 o 2.")
except ValueError:
    print("Entrada no valida. Escribe una temperatura numerica.")
