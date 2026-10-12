# Investigación: Automatización de Procesos con VBA en Excel

## 1. Definición
**VBA (Visual Basic for Applications)** es un lenguaje de programación integrado dentro de la suite de Microsoft Office. Su principal función es automatizar tareas repetitivas, crear funciones personalizadas (UDF) y diseñar interfaces de usuario dentro de hojas de cálculo de Excel.

---

## 2. Lógica de Funcionamiento
Las macros en VBA se estructuran mediante **procedimientos** (`Sub`) y **funciones** (`Function`). Mediante el objeto `Range` o `Cells`, el código puede interactuar directamente con celdas, filas, columnas y hojas completas sin intervención manual del usuario.

---

## 3. Ejemplo Conceptual en VBA

```vba
Sub SumarCeldas()
    Dim total As Double
    total = Range("A1").Value + Range("A2").Value
    Range("A3").Value = total
End Sub
```

---

## 4. Cuadro Comparativo: Uso Manual vs. Macros en VBA

| Criterio | Operación Manual en Excel | Automatización con VBA |
| :--- | :--- | :--- |
| **Velocidad** | Lenta y propensa a errores humanos. | Ejecución instantánea en milisegundos. |
| **Tareas Repetitivas** | Demanda tiempo constante del operario. | Se ejecuta con un solo botón o atajo de teclado. |
| **Escalabilidad** | Limitada al volumen que soporte la persona. | Capaz de procesar miles de registros de forma masiva. |

---

## 5. Análisis de Complejidad Temporal

* **Optimización:** Las macros mal optimizadas que seleccionan celdas visualmente (`Select`) ralentizan la ejecución. Al operar directamente con valores en memoria mediante arreglos o referencias de rango (`Cells`), la complejidad se reduce notablemente mejorando el rendimiento.

---

## 6. Conclusión
El dominio de VBA en Excel representa una herramienta de alto valor en el ámbito laboral y de desarrollo de software empresarial, permitiendo transformar hojas de cálculo estáticas en aplicaciones dinámicas y automatizadas.