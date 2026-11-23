' ==========================================
' Validación de Entradas Numéricas en VBA
' ==========================================

Sub ValidarCalificacionesColumnaA()
    Dim fila As Long
    Dim ultimaFila As Long
    Dim valorCelda As Variant
    
    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row
    
    For fila = 2 To ultimaFila
        valorCelda = Cells(fila, 1).Value
        
        If IsNumeric(valorCelda) Then
            If CDbl(valorCelda) >= 0 And CDbl(valorCelda) <= 5 Then
                Cells(fila, 2).Value = "Válido"
            Else
                Cells(fila, 2).Value = "Fuera de rango (0-5)"
            End If
        Else
            Cells(fila, 2).Value = "No numérico"
        End If
    Next fila
    
    MsgBox "Validación de datos finalizada.", vbInformation, "SENA ADSO"
End Sub