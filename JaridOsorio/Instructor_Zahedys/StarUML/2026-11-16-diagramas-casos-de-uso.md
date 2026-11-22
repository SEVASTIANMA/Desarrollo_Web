# Investigación: Diagramas de Casos de Uso en UML y StarUML

## 1. Definición
El **Diagrama de Casos de Uso** es una representación gráfica conductual de UML que describe cómo interactúan los actores externos (usuarios, roles o sistemas) con las funcionalidades clave de un sistema de software para lograr un objetivo específico.

---

## 2. Lógica del Modelado
1. **Identificación de Actores:** Se definen quiénes inician o participan en cada proceso sin entrar todavía en detalles internos de código.
2. **Definición de Casos de Uso:** Cada óvalo expresa una acción con valor observable para el actor, redactada con verbo en infinitivo más objeto (ej. `Generar reporte`).
3. **Relaciones Estructurales:** Se emplean asociaciones, `<<include>>` (dependencia obligatoria) y `<<extend>>` (comportamiento opcional o condicional).

---

## 3. Ejemplo Conceptual (Flujo de Caso de Uso)

```text
[Aprendiz] ---> (Registrar Práctica Diaria)
                      |
                      +--- <<include>> ---> (Validar Estructura de Archivo)