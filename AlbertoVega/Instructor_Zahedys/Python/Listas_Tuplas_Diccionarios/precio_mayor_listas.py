precios = [50000, 80000, 35000, 60000, 25000]

mayor = 50000

for precio in precios:
    if mayor < precio:
        mayor = precio

print(f"Precio mas alto: {mayor}")