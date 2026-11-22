# ==========================================
# Manejo de Estructuras JSON en Python
# ==========================================

import json

# Diccionario de datos para exportar
datos_aprendiz = {
    "nombre": "Jarid",
    "programa": "ADSO",
    "ficha": 3532730,
    "tecnologias": ["Python", "Dart", "VBA"]
}

# Convertir diccionario a formato JSON (Serialización)
json_string = json.dumps(datos_aprendiz, indent=4, ensure_ascii=False)
print("--- DATOS EN FORMATO JSON ---")
print(json_string)

# Guardar en un archivo simulado
with open("perfil_adso.json", "w", encoding="utf-8") as archivo:
    json.dump(datos_aprendiz, archivo, indent=4, ensure_ascii=False)

print("\n✅ Archivo JSON generado y guardado correctamente.")
