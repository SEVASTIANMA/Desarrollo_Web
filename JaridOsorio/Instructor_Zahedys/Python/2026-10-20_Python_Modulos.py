# ==========================================
# Uso de Módulos y Funciones Matemáticas en Python
# ==========================================

import math
import datetime

def calcular_operaciones_avanzadas(numero):
    raiz = math.sqrt(numero)
    potencia = math.pow(numero, 3)
    seno = math.sin(math.radians(numero))
    
    print(f"--- ANÁLISIS MATEMÁTICO (Número: {numero}) ---")
    print(f"Raíz cuadrada: {raiz:.2f}")
    print(f"Potencia al cubo: {potencia}")
    print(f"Seno (grados): {seno:.4f}")

# Registro de ejecución con fecha actual
fecha_actual = datetime.datetime.now()
print(f"Ejecutado el: {fecha_actual.strftime('%Y-%m-%d %H:%M:%S')}")

calcular_operaciones_avanzadas(9)
