# Investigación: Trazabilidad entre Casos de Uso y Diagramas de Clases en StarUML

## 1. Definición
La **trazabilidad entre casos de uso y diagramas de clases** consiste en mapear los requisitos funcionales definidos en los flujos de interacción hacia las entidades, atributos y métodos que implementan esa lógica dentro del modelo estructural del sistema.

---

## 2. Lógica de Trazabilidad
1. **Identificación de Entidades:** Cada sustantivo relevante en la descripción de un caso de uso suele corresponder a una clase candidata.
2. **Definición de Responsabilidades:** Las acciones o verbos del flujo se traducen en métodos asignados a la clase con mayor cohesión.
3. **Validación de Cardinalidades:** Las reglas del negocio determinan las multiplicidades entre clases antes de pasar al código.

---

## 3. Ejemplo Conceptual (Caso de Uso a Clases)

```text
Caso de Uso: Registrar Avance Diario
  ├── Clase: Aprendiz  --> + registrarAvance(avance)
  └── Clase: Avance    --> - fecha, - tema, + validar()

```

---

## 4. Cuadro Comparativo: Modelo Funcional vs. Modelo Estructural

| Criterio | Diagrama de Casos de Uso | Diagrama de Clases |
| :--- | :--- | :--- |
| **Perspectiva** | Externa / funcional (qué hace el sistema para el actor). | Interna / estructural (cómo se organizan datos y operaciones). |
| **Enfoque Temporal** | Flujos de interacción y eventos del usuario. | Estructura estática y relaciones entre objetos. |
| **Uso en Desarrollo** | Validación de alcance y requisitos con interesados. | Base directa para clases en Python, Dart o lenguajes POO. |

---

## 5. Análisis de Complejidad

* **Reducción de Desviaciones:** Mantener alineados los casos de uso y las clases en StarUML evita métodos huérfanos o lógica dispersa, disminuyendo errores de diseño al iniciar la codificación.

---

## 6. Conclusión
Vincular los diagramas de casos de uso con los diagramas de clases en StarUML da coherencia a todo el diseño orientado a objetos y facilita el paso ordenado hacia la implementación.