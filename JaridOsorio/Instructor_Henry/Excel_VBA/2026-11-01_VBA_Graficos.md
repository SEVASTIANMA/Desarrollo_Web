' ==========================================
' Creación de Gráficos Automáticos en Excel
' ==========================================

Sub GenerarGraficoRendimiento()
    Dim graficoObj As ChartObject
    
    ' Crear un objeto de gráfico en la hoja activa
    Set graficoObj = ActiveSheet.ChartObjects.Add(Left:=100, Width:=375, Top:=50, Height:=225)
    
    ' Establecer el rango de datos que alimentará el gráfico
    graficoObj.Chart.SetSourceData Source:=Range("A1:B10")
    
    ' Definir tipo de gráfico (ej. Columnas agrupadas)
    graficoObj.Chart.ChartType = xlColumnClustered
    
    MsgBox "Gráfico de rendimiento generado automáticamente.", vbInformation, "VBA Excel"
End Sub