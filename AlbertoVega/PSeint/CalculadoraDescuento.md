Algoritmo CalculadoraDescuento

// Este algoritmo permite calcular el costo final de una compra aplicando descuentos según el monto total y el tipo de cliente (Regular o VIP).

	Definir montoTotal, montoFinal, descuento Como Real
	Definir tipoCliente Como Cadena
	
	Escribir "Ingrese el monto total de la compra:"
	Leer montoTotal
	Escribir "Ingrese el tipo de cliente (VIP / Regular):"
	Leer tipoCliente
	
	tipoCliente <- Mayusculas(tipoCliente)
	
	Si montoTotal > 0 Entonces
		Si tipoCliente = "VIP" Entonces
			Si montoTotal >= 1000 Entonces
				descuento <- 0.20
			Sino
				descuento <- 0.10 
			FinSi
		Sino
			Si tipoCliente = "REGULAR" Entonces
				Si montoTotal >= 1000 Entonces
					descuento <- 0.05
				Sino
					descuento <- 0.00
				FinSi
			Sino
				Escribir "Tipo de cliente no reconocido. Se aplicará 0% de descuento."
				descuento <- 0.00
			FinSi
		FinSi
		
		montoFinal <- montoTotal - (montoTotal * descuento)
		Escribir "Porcentaje de descuento aplicado: ", descuento * 100, "%"
		Escribir "Total a pagar: $", montoFinal
	Sino
		Escribir "Error: El monto ingresado debe ser mayor a cero."
	FinSi
FinAlgoritmo