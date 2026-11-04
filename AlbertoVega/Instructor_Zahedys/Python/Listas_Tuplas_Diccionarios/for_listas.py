# Mostrar únicamente los videojuegos cuyo nombre tenga más de 7 caracteres.

juegos = [
    "Outlast",
    "Subnautica",
    "Fortnite",
    "FNAF",
    "Minecraft"
]

for juego in juegos:
    n = len(juego)
    if n > 7:
        print(juego)