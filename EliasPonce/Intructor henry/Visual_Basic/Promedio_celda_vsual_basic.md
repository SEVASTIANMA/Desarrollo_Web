Sub ProbarPromedio()
    ' Variable para almacenar el promedio
    Dim resultadoPromedio As Double
    
    ' Calcula el promedio de las celdas A1 hasta A4 de la hoja activa
    resultadoPromedio = CalcularPromedioVBA(Range("A1:A4"))
    
    ' Mostrar resultado
    MsgBox "El promedio del rango A1:A4 es: " & resultadoPromedio, vbInformation, "Resultado Promedio"
End Sub

' Función que acepta un rango de Excel (Range) y calcula su media aritmética
Function CalcularPromedioVBA(celdas As Range) As Double
    Dim celda As Range
    Dim sumaTotal As Double
    Dim contador As Long
    
    sumaTotal = 0
    contador = 0
    
    ' Recorre cada celda en el rango seleccionado
    For Each celda In celdas
        ' Verifica que la celda contenga un número y no esté vacía
        If IsNumeric(celda.Value) And Not IsEmpty(celda.Value) Then
            sumaTotal = sumaTotal + celda.Value
            contador = contador + 1
        End If
    Next celda
    
    ' Evita errores de división por cero si el rango está vacío
    If contador > 0 Then
        CalcularPromedioVBA = sumaTotal / contador
    Else
        CalcularPromedioVBA = 0
    End If
End Function
