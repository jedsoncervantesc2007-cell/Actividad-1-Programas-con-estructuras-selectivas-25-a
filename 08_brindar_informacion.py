"""
Programa 8: Muestra informacion sobre artistas, peliculas y series con match-case.
"""

tema = input(
    "Escribe Shakira, Bad Bunny, Inception, Titanic o Breaking Bad: "
).strip().casefold()

match tema:
    case "shakira":
        print("Shakira: cantante y compositora colombiana.")
        print("Es conocida por combinar pop latino y ritmos internacionales.")
    case "bad bunny":
        print("Bad Bunny: cantante puertorriqueno de musica urbana.")
        print("Su trabajo incluye regueton y trap latino.")
    case "inception":
        print("Inception (2010): pelicula de ciencia ficcion dirigida por Christopher Nolan.")
        print("Trata sobre un equipo que se infiltra en los suenos.")
    case "titanic":
        print("Titanic (1997): pelicula dramatica dirigida por James Cameron.")
        print("La historia de amor ocurre durante el viaje del RMS Titanic.")
    case "breaking bad":
        print("Breaking Bad: serie de drama creada por Vince Gilligan.")
        print("Sigue a un profesor de quimica que empieza a fabricar metanfetamina.")
    case _:
        print("No tengo informacion de ese tema. Prueba uno de los cinco ejemplos.")
