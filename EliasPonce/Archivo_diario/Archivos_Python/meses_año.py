# 1. Pedir el número al usuario y convertirlo en entero
mes = int(input("Introduce el número de mes (1-12): "))

# 2. Comprobar el número e imprimir el nombre correspondiente
if mes == 1:
    print("El mes seleccionado es Enero")
elif mes == 2:
    print("El mes seleccionado es Febrero")
elif mes == 3:
    print("El mes seleccionado es   Marzo")
elif mes == 4:
    print("El mes seleccionado es Abril")
elif mes == 5:
    print("El mes seleccionado es Mayo")
elif mes == 6:
    print("El mes seleccionado es Junio")
elif mes == 7:
    print("El mes seleccionado es Julio")
elif mes == 8:
    print("El mes seleccionado es Agosto")
elif mes == 9:
    print("El mes seleccionado es Septiembre")
elif mes == 10:
    print("El mes seleccionado es Octubre")
elif mes == 11:
    print("El mes seleccionado es Noviembre")
elif mes == 12:
    print("El mes seleccionado es Diciembre")
else:
    # Si no es ningún número del 1 al 12, muestra el error
    print("Error al teclear el mes. Debe ser un número entre 1 y 12.")