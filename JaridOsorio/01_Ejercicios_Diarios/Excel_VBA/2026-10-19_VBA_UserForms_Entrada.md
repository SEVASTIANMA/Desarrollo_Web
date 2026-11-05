' ==========================================
' Captura de Datos desde Formulario VBA
' ==========================================

Sub AbrirFormularioRegistro()
    ' Muestra el formulario personalizado para ingresar aprendices
    ' (Asegurarse de tener creado el UserForm1 en el proyecto)
    UserForm1.Show
End Sub

' Código interno dentro del botón del UserForm1:
Private Sub btnGuardar_Click()
    Dim ultimaFila As Long
    
    ' Encontrar la última fila con datos en la columna A
    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row + 1
    
    ' Asignar valores desde las cajas de texto (TextBox)
    Cells(ultimaFila, 1).Value = txtNombre.Text
    Cells(ultimaFila, 2).Value = txtFicha.Text
    
    MsgBox "Aprendiz registrado en la fila " & ultimaFila, vbInformation, "SENA ADSO"
    Unload Me
End Sub
