' ==========================================
' Conteo de Estados de Actividades en VBA
' ==========================================

Sub ContarEstadosActividades()
    Dim fila As Long
    Dim ultimaFila As Long
    Dim totalCompletadas As Long
    Dim totalPendientes As Long
    
    ultimaFila = Cells(Rows.Count, 2).End(xlUp).Row
    totalCompletadas = 0
    totalPendientes = 0
    
    For fila = 2 To ultimaFila
        Select Case LCase(Trim(Cells(fila, 2).Value))
            Case "completada", "revisada"
                totalCompletadas = totalCompletadas + 1
            Case "pendiente"
                totalPendientes = totalPendientes + 1
        End Select
    Next fila
    
    Range("D2").Value = "Completadas/Revisadas"
    Range("E2").Value = totalCompletadas
    Range("D3").Value = "Pendientes"
    Range("E3").Value = totalPendientes
    
    MsgBox "Resumen generado: " & totalCompletadas & " completadas, " & totalPendientes & " pendientes.", vbInformation, "ADSO"
End Sub