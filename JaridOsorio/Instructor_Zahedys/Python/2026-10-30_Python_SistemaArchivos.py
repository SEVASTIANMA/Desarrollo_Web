# ==========================================
# Interacción con el Sistema Operativo en Python
# ==========================================

import os

def verificar_entorno_trabajo():
    # Obtener el directorio actual de trabajo
    directorio_actual = os.getcwd()
    print(f"📁 Directorio actual: {directorio_actual}")
    
    # Listar elementos de la carpeta actual
    elementos = os.listdir(directorio_actual)
    print(f"📋 Elementos encontrados en la ruta: {len(elementos)} elementos.")
    
    # Crear una carpeta de respaldo si no existe
    carpeta_respaldo = "Respaldo_ADSO"
    if not os.path.exists(carpeta_respaldo):
        os.makedirs(carpeta_respaldo)
        print(f"✅ Carpeta '{carpeta_respaldo}' creada exitosamente.")
    else:
        print(f"ℹ️ La carpeta '{carpeta_respaldo}' ya existe.")

verificar_entorno_trabajo()