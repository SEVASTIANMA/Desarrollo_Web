Sub ProbarInvertirTexto()
    ' Cadena de texto de prueba
    Dim textoOriginal As String
    Dim textoInvertido As String
    
    textoOriginal = "Excel VBA"
    
    ' Llamada a la función
    textoInvertido = InvertirTextoVBA(textoOriginal)
    
    ' Mostrar resultados
    MsgBox "Original: " & textoOriginal & vbCrLf & "Invertido: " & textoInvertido, vbInformation, "Texto Invertido"
End Sub

' Función independiente para dar la vuelta al texto usando las herramientas nativas de VBA
Function InvertirTextoVBA(texto As String) As String
    InvertirTextoVBA = StrReverse(texto)
End Function
