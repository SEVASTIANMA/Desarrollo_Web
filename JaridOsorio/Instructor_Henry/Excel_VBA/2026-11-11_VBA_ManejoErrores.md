' ==========================================
' Control de Excepciones y Errores en VBA
' ==========================================

Sub OperacionSeguraVBA()
    On Error GoTo ManejadorError
    
    Dim valorNumerico As Double
    ' Provocar un error intencional de división por cero
    valorNumerico = 100 / 0
    
    Exit Sub

ManejadorError:
    MsgBox "Ocurrió un error en la ejecución: " & Err.Description, vbCritical, "Error Detectado"
    ' Limpiar el error
    Err.Clear
End Sub