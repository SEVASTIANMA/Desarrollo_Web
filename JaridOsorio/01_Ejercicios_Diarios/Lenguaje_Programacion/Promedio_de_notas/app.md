# Ejercicio realizado en Visual Basic

Sub CalcularPromedioNotas()
    Dim nota1 As Double
    Dim nota2 As Double
    Dim nota3 As Double
    Dim nota4 As Double
    Dim nota5 As Double
    Dim sumaNotas As Double
    Dim promedio As Double

    ' 1. Solicitar las 5 notas mediante una ventana emergente (InputBox)
    nota1 = CDbl(InputBox("Ingresa la nota 1:", "Promedio"))
    nota2 = CDbl(InputBox("Ingresa la nota 2:", "Promedio"))
    nota3 = CDbl(InputBox("Ingresa la nota 3:", "Promedio"))
    nota4 = CDbl(InputBox("Ingresa la nota 4:", "Promedio"))
    nota5 = CDbl(InputBox("Ingresa la nota 5:", "Promedio"))

    ' 2. Sumar las notas de manera secuencial
    sumaNotas = nota1 + nota2 + nota3 + nota4 + nota5

    ' 3. Calcular el promedio dividiendo entre 5
    promedio = sumaNotas / 5

    ' 4. Mostrar el resultado en un mensaje emergente
    MsgBox "El promedio final de las 5 notas es: " & promedio, vbInformation, "Resultado del Promedio"
End Sub