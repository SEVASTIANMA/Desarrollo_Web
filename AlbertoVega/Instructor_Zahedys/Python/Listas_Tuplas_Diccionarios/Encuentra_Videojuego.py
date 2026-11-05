juegos = ["Outlast", "Minecraft", "FNAF", "Subnautica"]
print("Encontrador de juegos")
for juego in juegos:
    if juego == "FNAF":
        print(f"¡Juego encontrado! {juego}")
print("---")
juegos2 = ["FNAF", "Outlast", "FNAF", "Minecraft", "FNAF", "Subnautica"]
print("Contador de juegos")
cont = 0
for juego in juegos2:
    if juego == "FNAF":
        cont += 1
print(f"Subnautica fue encontrado {cont} veces")