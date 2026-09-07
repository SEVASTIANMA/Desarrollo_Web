Algoritmo Factura_promedio
	
		// Definir variables
		Definir prod1, prod2, prod3 Como Caracter
		Definir precio1, precio2, precio3 Como Real
		Definir total, promedio Como Real
		
		// Entrada de datos del primer producto
		Escribir "Ingrese el nombre del primer producto:"
		Leer prod1
		Escribir "Ingrese el precio de ", prod1, ":"
		Leer precio1
		
		// Entrada de datos del segundo producto
		Escribir "Ingrese el nombre del segundo producto:"
		Leer prod2
		Escribir "Ingrese el precio de ", prod2, ":"
		Leer precio2
		
		// Entrada de datos del tercer producto
		Escribir "Ingrese el nombre del tercer producto:"
		Leer prod3
		Escribir "Ingrese el precio de ", prod3, ":"
		Leer precio3
		
		// Procesar los datos (Cálculos)
		total <- precio1 + precio2 + precio3
		promedio <- total / 3
		
		// Salida de resultados (Factura)
		Escribir ""
		Escribir "=== FACTURA DE COMPRA ==="
		Escribir "1. ", prod1, " ----------- $", precio1
		Escribir "2. ", prod2, " ----------- $", precio2
		Escribir "3. ", prod3, " ----------- $", precio3
		Escribir "-------------------------"
		Escribir "TOTAL A PAGAR: -------- $", total
		Escribir "PROMEDIO POR PRODUCTO:  $", promedio
		Escribir "========================="
FinAlgoritmo
