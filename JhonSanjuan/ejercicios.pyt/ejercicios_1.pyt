Nom = str(input("Digite el nombre del producto: "))
Cant = float(input("Digite la cantidad de productos: "))
ValUnitario = float(input("Digite el valor unitario del producto: "))

print(f"El Subtotal del producto {Nom} es: {Cant * ValUnitario}")
print(f"El IVA del producto {Nom} es: {(Cant * ValUnitario) * 0.19}")
print(f"El total del producto {Nom} es: {(Cant * ValUnitario) + ((Cant * ValUnitario) * 0.19)}")