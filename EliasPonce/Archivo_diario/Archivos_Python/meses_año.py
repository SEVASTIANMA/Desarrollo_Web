# 1. Pedir el número al usuario y convertirlo en entero
mes = int(input("Introduce el número de mes (1-12): "))

# 2. Comprobar el número e imprimir el nombre correspondiente
if mes == 1:
    print("Enero")
elif mes == 2:
    print("Febrero")
elif mes == 3:
    print("Marzo")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Mayo")
elif mes == 6:
    print("Junio")
elif mes == 7:
    print("Julio")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Septiembre")
elif mes == 10:
    print("Octubre")
elif mes == 11:
    print("Noviembre")
elif mes == 12:
    print("Diciembre")
else:
    # Si no es ningún número del 1 al 12, muestra el error
    print("Error al teclear el mes. Debe ser un número entre 1 y 12.")