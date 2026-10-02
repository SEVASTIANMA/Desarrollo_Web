// 1. Subproceso tipo Función para calcular el descuento
Funcion descuento <- calcularDescuento(valorCompra, categoriaMembresia)
    Definir descuento Como Real
    
    // Convertir a mayúsculas para evitar errores si ingresan 'a', 'b' o 'c'
    Segun Mayusculas(categoriaMembresia) Hacer
        'A':
            descuento <- valorCompra * 0.20
        'B':
            descuento <- valorCompra * 0.15
        'C':
            descuento <- valorCompra * 0.10
        De Otro Modo:
            descuento <- 0
    FinSegun
FinFuncion

// 2. Subproceso tipo Procedimiento para mostrar el ticket
SubProceso MostrarResumen(valorOriginal, descuentoCalculado, montoFinal)
    Escribir "======================================="
    Escribir "          TICKET DE COMPRA             "
    Escribir "======================================="
    Escribir "Valor original de compra: $", valorOriginal
    Escribir "Descuento aplicado:       $", descuentoCalculado
    Escribir "---------------------------------------"
    Escribir "Total final a pagar:      $", montoFinal
    Escribir "======================================="
FinSubProceso

// Algoritmo Principal
Algoritmo TiendaDepartamental
    Definir valorCompra, descuento, totalPagar Como Real
    Definir categoriaMembresia Como Caracter
    
    // Solicitar datos al usuario
    Escribir "Ingrese el valor total de la compra:"
    Leer valorCompra
    
    Escribir "Ingrese la categoría de membresía (A, B, C o otra):"
    Leer categoriaMembresia
    
    // Llamada a la función para obtener el descuento
    descuento <- calcularDescuento(valorCompra, categoriaMembresia)
    
    // Calcular el total a pagar
    totalPagar <- valorCompra - descuento
    
    // Llamada al procedimiento para mostrar los resultados
    MostrarResumen(valorCompra, descuento, totalPagar)
FinAlgoritmo