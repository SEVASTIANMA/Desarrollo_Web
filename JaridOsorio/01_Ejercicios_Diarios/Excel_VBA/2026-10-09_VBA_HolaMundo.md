' ==========================================
' Introducción a Macros y VBA en Excel
' ==========================================

Sub SaludoSENAADSO()
    Dim mensaje As String
    mensaje = "¡Bienvenido al entorno de desarrollo VBA en Excel!"
    
    ' Escribir en la celda A1 de la hoja activa
    Cells(1, 1).Value = "Módulo ADSO"
    Cells(1, 2).Value = mensaje
    
    MsgBox "Datos insertados correctamente en la hoja.", vbInformation, "Aviso SENA"
End Sub
