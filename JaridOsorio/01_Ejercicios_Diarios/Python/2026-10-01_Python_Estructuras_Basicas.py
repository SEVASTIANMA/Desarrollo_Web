# ==========================================
# Ejercicio 1: Introducción a Python en ADSO
# Manejo de listas, condicionales y bucles
# ==========================================

# 1. Definición de una lista (equivalente a vectores en PSeInt)
tecnologias = ["Python", "Dart", "Excel VBA", "Git"]

print("--- TECNOLOGÍAS DEL NUEVO MÓDULO ---")
for i, tech in enumerate(tecnologias, start=1):
    print(f"{i}. {tech}")

# 2. Función para evaluar calificaciones (Condicionales)
def evaluar_rendimiento(calificacion):
    if calificacion >= 4.5:
        return "Sobresaliente 🚀"
    elif calificacion >= 3.5:
        return "Aprobado con buen nivel 👍"
    else:
        return "Requiere refuerzo o mejora ⚠️"

# 3. Prueba de la función
nota_final = 4.2
resultado = evaluar_rendimiento(nota_final)
print(f"\nEvaluación final (Nota {nota_final}): {resultado}")