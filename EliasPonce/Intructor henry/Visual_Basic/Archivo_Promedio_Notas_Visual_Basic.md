Sub CalcularPromedio()
    n1 = CDbl(InputBox("Nota 1:"))
    n2 = CDbl(InputBox("Nota 2:"))
    n3 = CDbl(InputBox("Nota 3:"))
    n4 = CDbl(InputBox("Nota 4:"))
    n5 = CDbl(InputBox("Nota 5:"))
    
    promedio = (n1 + n2 + n3 + n4 + n5) / 5
    
    MsgBox "El promedio final de las 5 notas es: " & promedio
End Sub