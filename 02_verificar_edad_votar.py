"""
Programa 2: Verifica si una persona cumple la edad para votar.
"""

EDAD_MINIMA = 18
EDAD_MAXIMA_RAZONABLE = 120

try:
    edad = int(input("Ingresa tu edad: "))

    if edad < 0 or edad > EDAD_MAXIMA_RAZONABLE:
        print("Edad no valida.")
    elif edad >= EDAD_MINIMA:
        print("Puedes votar por edad.")
    else:
        print("Aun no tienes la edad minima para votar.")
except ValueError:
    print("Entrada no valida. Escribe tu edad en numeros enteros.")
