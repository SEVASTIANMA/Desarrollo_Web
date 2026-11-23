' ==========================================
' Automatización de Hojas y Copia de Datos en VBA
' ==========================================

Sub OrganizarDatosADSO()
    Dim wsOrigen As Worksheet
    Dim wsDestino As Worksheet
    
    Set wsOrigen = ActiveSheet
    
    ' Copiar encabezados a otra hoja o sección
    wsOrigen.Range("A1:C1").Copy
    
    ' Crear o seleccionar celda de destino
    Range("E1").Select
    ActiveSheet.Paste
    
    MsgBox "Estructura de datos organizada con éxito en Excel.", vbInformation, "ADSO SENA"
End Sub