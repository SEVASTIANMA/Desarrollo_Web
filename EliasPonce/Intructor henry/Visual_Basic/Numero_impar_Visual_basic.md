Sub ProbarParidad()
    ' Variable de prueba
    Dim numero As Integer
    numero = 7
    
    ' Llamada a la función dentro de una estructura condicional
    If EsParVBA(numero) Then
        MsgBox "El número " & numero & " es PAR.", vbInformation, "Resultado Paridad"
    Else
        MsgBox "El número " & numero & " es IMPAR.", vbExclamation, "Resultado Paridad"
    End If
End Sub

' Función independiente para validar paridad
Function EsParVBA(numero As Integer) As Boolean
    If numero Mod 2 = 0 Then
        EsParVBA = True
    Else
        EsParVBA = False
    End If
End Function
