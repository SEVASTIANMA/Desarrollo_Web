# Ejercicio Práctico StarUML: Diagrama de Casos de Uso

## Objetivo
Modelar las interacciones funcionales entre los actores del sistema y los procesos principales antes de codificar.

## Elementos del Diagrama en StarUML
- **Actor:** `Aprendiz ADSO` / `Instructor SENA` (representado con el ícono de actor en la paleta UML).
- **Casos de Uso:**
  1. `Registrar avance diario`
  2. `Consultar retroalimentación`
  3. `Sincronizar repositorio`
- **Relaciones:** Asociación simple entre actor y caso de uso; `<<include>>` cuando un paso obligatorio forma parte del flujo (por ejemplo, `Validar formato de archivo`).

## Especificación Breve del Caso de Uso Principal
- **Caso de uso:** Registrar avance diario
- **Actor principal:** Aprendiz ADSO
- **Flujo normal:**
  1. El aprendiz abre su entorno de trabajo local.
  2. Crea el archivo correspondiente a la fecha y temática.
  3. Verifica sintaxis y guarda los cambios en el repositorio.