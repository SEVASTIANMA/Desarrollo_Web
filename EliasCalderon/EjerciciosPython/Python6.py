materias = int(input('Cuantas materias tienes matriculadas?'))
materiasM = 100000
cantidad = materias * materiasM
print (cantidad)
promedio = float(input('Cual es tu promedio? '))
descuento = cantidad * 0.25
iva = cantidad * 0.10
preciofinal = cantidad - descuento
pecueca = cantidad + iva
if promedio >= 4.5:
    print (f'Su beneficio por su promedio es el valor a pagar de: {preciofinal}')
else:
    print (f'Su valor a pagar es {pecueca} no se aplica descuento.')
    

