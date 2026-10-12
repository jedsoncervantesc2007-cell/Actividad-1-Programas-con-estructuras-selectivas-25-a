"""
Programa 3: Convierte una calificacion numerica en una letra.
"""

try:
    calificacion = float(input("Ingresa una calificacion (0-100): "))

    if not 0 <= calificacion <= 100:
        print("La calificacion debe estar entre 0 y 100.")
    elif calificacion >= 90:
        print("Letra: A")
    elif calificacion >= 80:
        print("Letra: B")
    elif calificacion >= 70:
        print("Letra: C")
    elif calificacion >= 60:
        print("Letra: D")
    else:
        print("Letra: F")
except ValueError:
    print("Entrada no valida. Escribe un numero.")
