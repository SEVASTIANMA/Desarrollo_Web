# ==========================================
# Estructuras de Control (If / Elif / Else)
# ==========================================

def evaluar_nota(nota):
    if nota >= 4.5:
        return "Excelente desempeño (Aprobado con honores)"
    elif nota >= 3.5:
        return "Aprobado satisfactoriamente"
    else:
        return "No aprobado - Requiere plan de mejoramiento"

calificacion_actual = 4.2
resultado = evaluar_nota(calificacion_actual)

print(f"Calificación: {calificacion_actual}")
print(f"Estado: {resultado}")