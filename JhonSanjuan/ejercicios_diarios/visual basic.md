Sub CalcularPromedio()

    MsgBox "Ingrese a continuacion las 5 notas del periodo academico:"

    nota1 = InputBox("[1]:")
    nota2 = InputBox("[2]:")
    nota3 = InputBox("[3]:")
    nota4 = InputBox("[4]:")
    nota5 = InputBox("[5]:")

    (En visual basic para convertir de string a int se escribe como "CInt")
    suma = CInt(nota1) + CInt(nota2) + CInt(nota3) + CInt(nota4) + CInt(nota5)

    promedioFinal = suma / 5

    MsgBox "Nota final: " & promedioFinal

End Sub
