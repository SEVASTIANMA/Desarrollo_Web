' ==========================================
' Rellenar datos automáticamente con Bucles en VBA
' ==========================================

Sub GenerarTablaExcel()
    Dim i As Integer
    
    ' Limpiar celdas previas de la columna A
    Columns("A:A").Clear
    
    ' Bucle para rellenar celdas del 1 al 10
    For i = 1 To 10
        Cells(i, 1).Value = "Fila número: " & i
    Next i
    
    MsgBox "¡Tabla generada con éxito en Excel!", vbGreen, "Proceso Finalizado"
End Sub
