# Descripción del Algoritmo: Control de Ventas, Descuentos y Obsequios

Este algoritmo automatiza el proceso de facturación para la compra de un producto en cantidad. Su objetivo principal es calcular el monto total a pagar por un cliente, aplicando un porcentaje de descuento variable y otorgando unidades de obsequio de acuerdo con la cantidad de docenas adquiridas.

---

## Explicación Paso a Paso del Código

El algoritmo se ejecuta de manera secuencial a través de las siguientes fases:

### 1. Entrada de Datos
El programa solicita al usuario ingresar dos valores clave para iniciar los cálculos:
* **cantidad**: El número total de unidades que el cliente va a comprar.
* **precio**: El valor económico de una sola unidad del producto.

### 2. Cálculos Iniciales (Monto Base y Docenas)
* **monto = cantidad * precio**: Multiplica las unidades por su precio unitario para obtener el subtotal de la compra antes de aplicar los beneficios.
* **docena = trunc(cantidad / 12)**: Divide la cantidad de productos entre 12 para saber cuántas docenas se están comprando. Utiliza la función `trunc` (truncar) para conservar únicamente el número entero de docenas, ignorando los productos sueltos sobrantes.

### 3. Lógica de Obsequios
El algoritmo evalúa si el cliente tiene derecho a productos de regalo mediante una condición:
* **Si compra más de 3 docenas (docena > 3)**: Se le regala una unidad por cada docena en exceso. El cálculo se realiza con la fórmula `obsequio = docena - 3`.
* *Nota:* Si compra 3 docenas o menos, la variable `obsequio` no se calcula en esta estructura, por lo que se asume vacía o en cero.

### 4. Lógica de Descuentos
El programa aplica una política de descuentos escalonada dependiendo de la cantidad de docenas:
* **Descuento Especial (15%)**: Si el cliente adquiere más de 3 docenas, se le descuenta el 15% del monto base (`monto * 15/100`).
* **Descuento Estándar (10%)**: Si compra 3 docenas o menos, se le aplica únicamente el 10% del monto base (`monto * 10/100`).

### 5. Cálculo Final y Salida de Resultados
Se determina el neto a pagar restando el beneficio obtenido (`valortotal = monto - descuento`) y finalmente se imprimen en pantalla los siguientes resultados para el usuario:
1. **Monto a pagar:** El subtotal inicial sin descuentos.
2. **Su descuento es:** El dinero ahorrado gracias al porcentaje aplicado (10% o 15%).
3. **Total a pagar:** La cantidad final de dinero que el cliente debe abonar.
4. **Unidades obsequiadas:** La cantidad de productos de regalo que se lleva el cliente.



Algoritmo productos
	escribir " Cuantos productos adquirio:  "
	leer cantidad
	Escribir " valor por unidad del producto: "
	leer precio
	
	monto = cantidad * precio
	docena = trunc(cantidad / 12)
	si docena > 3 Entonces
		obsequio = docena - 3
	FinSi
	
	si docena > 3 Entonces
		descuento = (monto * 15/100)
	SiNo
		descuento = (monto * 10/100)
		
	FinSi
	valortotal = monto - descuento
	escribir "Monto a pagar: " monto
	escribir "Su descuento es: " descuento
	Escribir "Total a pagar: " valortotal
	escribir " Unidades obsequiadas: " obsequio
FinAlgoritmo