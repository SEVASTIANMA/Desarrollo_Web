' ==========================================
' Estructuras de Control Avanzadas en VBA
' ==========================================

Sub EvaluarRendimientoAprendiz()
    Dim nota As Double
    Dim fila As Integer
    
    For fila = 2 To 6
        nota = Cells(fila, 2).Value
        
        ' Evaluación con Select Case
        Select Case nota
            Case 4.5 To 5.0
                Cells(fila, 3).Value = "Excelente"
            Case 3.5 To 4.4
                Cells(fila, 3).Value = "Satisfactorio"
            Case 0.0 To 3.4
                Cells(fila, 3).Value = "Deficiente"
            Case Else
                Cells(fila, 3).Value = "Nota inválida"
        End Select
    Next fila
    
    MsgBox "Evaluación de notas completada.", vbInformation, "ADSO SENA"
End Sub