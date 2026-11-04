# crea un programa que cuente cuántos videojuegos tienen más de 7 caracteres y muestre el total al final.

juegos = [
    "Outlast",
    "Subnautica",
    "Fortnite",
    "FNAF",
    "Minecraft"
]

cont = 0

for juego in juegos:
    n = len(juego)
    if n > 7:
        print(juego)
        cont+=1

print(f"Total de videojuegos: {cont}")