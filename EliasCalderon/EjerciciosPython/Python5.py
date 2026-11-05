litros = 0
litro = 5000
total = 0
contGente = 0
totallitros = 0
mayorque3 = 0
totalpreci = 0 
while totalpreci <= 1000000:
    ter = int(input('Digite la cant. de litros que quieres comprar'))
    print ('El precio por litro es : $5.000 ')
    contGente = contGente + 1
    preciofin = ter * litro
    print (f'usted va adquirir {ter} litros de desinfectante. ')
    print (f'El precio final es ${preciofin}.')
    totallitros = totallitros + ter
    totalpreci = totalpreci + preciofin
    if preciofin >= 300000:
        mayorque3 = mayorque3 + 1

print (f'El total de facturas fue de {contGente}')
print (f'El total de litros vendidos fue de l {totallitros}')
if mayorque3 > 0:
    print (f'El total de facturas > a 300mil fue de {mayorque3}')



'''
# Explicacion del Algoritmo de Control de Ventas

Este algoritmo en Python simula un sistema automatizado de facturacion y control de ventas para una tienda de desinfectantes. Su objetivo principal es registrar las compras de los clientes de forma continua hasta alcanzar una meta de recaudacion de dinero, generando estadisticas al final del proceso.

---

## Objetivo General
Registrar las ventas de desinfectante (a $5,000 el litro) y acumular los datos de los clientes hasta que las ventas totales superen el $1,000,000.

---

## Componentes del Codigo

### 1. Inicializacion de Variables
El programa comienza preparando los contadores y configurando los valores iniciales:
* litro = 5000: Define el precio fijo por cada litro de desinfectante.
* contGente: Cuenta el numero total de clientes (facturas realizadas).
* totallitros: Acumula la cantidad total de litros vendidos entre todos los clientes.
* totalpreci: Acumula el dinero total recaudado por la tienda.
* mayorque3: Cuenta cuantas facturas individuales tuvieron un costo de $300,000 o mas.

### 2. El Ciclo de Control (while)
El algoritmo utiliza un bucle "while totalpreci <= 1000000:". Esto significa que el programa se repetira e interrogara a cliente tras cliente mientras el dinero total recaudado sea menor o igual a un millon de pesos. En cuanto se supera esa meta, el ciclo se detiene.

### 3. Procesamiento por Cliente (Dentro del Bucle)
Por cada cliente que interactua con el sistema, se realizan los siguientes pasos:
1. Entrada de datos: Se solicita ingresar la cantidad de litros que desea comprar (ter).
2. Calculo financiero: Multiplica los litros ingresados por el precio base para obtener el precio final de esa compra (preciofin = ter * litro).
3. Retroalimentacion: Muestra en pantalla un mensaje confirmando los litros adquiridos y el precio total a pagar por ese cliente.
4. Actualizacion de estadisticas:
   * Se suma 1 al contador de clientes.
   * Se añaden los litros de esta compra al total general (totallitros).
   * Se añade el dinero de esta compra a la caja de la tienda (totalpreci).
5. Filtro de compras grandes (if): Si el precio de la factura es mayor o igual a $300,000 (equivalente a comprar 60 litros o mas), el contador mayorque3 se incrementa en 1.

### 4. Reporte Final
Al finalizar el proceso (cuando se rompe el ciclo while), el programa imprime en pantalla el resumen definitivo:
* El total de facturas emitidas.
* La cantidad total de litros desinfectantes vendidos.
* La cantidad de facturas que superaron los $300,000 (solo si hubo alguna).

---

## Nota Tecnica sobre la Indentacion
En la version original del codigo, los print del reporte final se encuentran dentro del ciclo while. Esto causa que el reporte final se imprima repetidamente cada vez que pasa un cliente. 

Para que funcione correctamente como un cierre de caja final, dichos mensajes deben extraerse del bucle removiendo sus espacios al inicio (alineandolos a la izquierda).

'''