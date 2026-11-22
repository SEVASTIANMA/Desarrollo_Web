' ==========================================
' Creación de Función Personalizada (UDF) en VBA
' ==========================================

Function CalcularPromedioADSO(nota1 As Double, nota2 As Double, nota3 As Double) As String
    Dim promedio As Double
    promedio = (nota1 + nota2 + nota3) / 3
    
    ' Retornar el promedio formateado con su respectivo estado
    If promedio >= 3.5 Then
        CalcularPromedioADSO = "Aprobado (" & Format(promedio, "0.0") & ")"
    Else
        CalcularPromedioADSO = "Reprobado (" & Format(promedio, "0.0") & ")"
    End If
End Function