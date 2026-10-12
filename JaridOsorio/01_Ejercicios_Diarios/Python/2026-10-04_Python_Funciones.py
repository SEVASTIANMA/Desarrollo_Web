# ==========================================
# Creación y Uso de Funciones en Python
# ==========================================

# Función para calcular el promedio de tres notas
def calcular_promedio(nota1, nota2, nota3):
    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    return round(promedio, 2)

# Función con condicional para validar aprobación
def validar_estado_academico(promedio):
    if promedio >= 3.5:
        return "APROBADO"
    else:
        return "REPROBADO"

# Ejecución principal
n1, n2, n3 = 4.2, 4.8, 3.9
promedio_final = calcular_promedio(n1, n2, n3)
estado = validar_estado_academico(promedio_final)

print("--- RESULTADO DE EVALUACIÓN ---")
print(f"Notas: {n1}, {n2}, {n3}")
print(f"Promedio Final: {promedio_final}")
print(f"Estado: {estado}")