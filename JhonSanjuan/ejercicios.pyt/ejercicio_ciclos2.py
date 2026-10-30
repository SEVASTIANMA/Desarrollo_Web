
cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años? "))

for i in range(1, años + 1):
    cantidad = cantidad * (1 + interes / 100)
    print("Capital tras", i, "años:", round(cantidad, 2))
