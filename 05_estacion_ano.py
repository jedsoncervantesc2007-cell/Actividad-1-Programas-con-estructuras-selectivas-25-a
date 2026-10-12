"""
Programa 5: Determina la estacion del ano mediante match-case.
"""

try:
    mes = int(input("Ingresa el numero de mes (1-12): "))

    match mes:
        case 3 | 4 | 5:
            print("Estacion: Primavera")
        case 6 | 7 | 8:
            print("Estacion: Verano")
        case 9 | 10 | 11:
            print("Estacion: Otono")
        case 12 | 1 | 2:
            print("Estacion: Invierno")
        case _:
            print("Mes no valido. Ingresa un numero del 1 al 12.")
except ValueError:
    print("Entrada no valida. Escribe un numero entero.")
