' ==========================================
' Recorrer filas dinámicamente con Do While
' ==========================================

Sub ProcesarFilasVacias()
    Dim fila As Integer
    fila = 1
    
    ' Recorre celdas de la columna A hasta encontrar una celda vacía
    Do While Not IsEmpty(Cells(fila, 1))
        Cells(fila, 2).Value = "Procesado ADSO"
        fila = fila + 1
    Loop
    
    MsgBox "Proceso de filas completado con éxito.", vbInformation, "VBA Excel"
End Sub