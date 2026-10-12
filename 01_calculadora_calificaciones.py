"""
Programa 1: Calculadora de calificaciones finales.
Calcula el promedio ponderado de parciales, proyecto y examen final.
"""

PESO_PARCIALES = 0.40
PESO_PROYECTO = 0.30
PESO_EXAMEN = 0.30


def pedir_calificacion(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if 0 <= valor <= 100:
                return valor
            print("La calificacion debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada no valida. Escribe un numero.")


parciales = pedir_calificacion("Calificacion de parciales (0-100): ")
proyecto = pedir_calificacion("Calificacion del proyecto (0-100): ")
examen = pedir_calificacion("Calificacion del examen final (0-100): ")

calificacion_final = (
    parciales * PESO_PARCIALES
    + proyecto * PESO_PROYECTO
    + examen * PESO_EXAMEN
)

print(f"Calificacion final: {calificacion_final:.2f}")
