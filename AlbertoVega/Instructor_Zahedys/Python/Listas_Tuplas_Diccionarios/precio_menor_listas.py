precios = [50000, 80000, 35000, 60000, 25000]

menor = 50000

for precio in precios:
    if menor > precio:
        menor = precio

print(f"El precio mas bajo: {menor}")