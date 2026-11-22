# Investigación: Diagramas de Clases y Relaciones en UML

## 1. Definición
El **Diagrama de Clases** es un diagrama estructural de UML que describe las clases de un sistema, sus atributos, operaciones (métodos) y las relaciones existentes entre ellas, sirviendo como base directa para la programación orientada a objetos.

---

## 2. Lógica de las Relaciones Principales
1. **Asociación:** Conexión estructural entre clases (con cardinalidad como `1` a `0..*`).
2. **Herencia (Generalización):** Una subclase hereda atributos y comportamientos de una superclase (`es un`).
3. **Agregación y Composición:** Representan relaciones todo-parte; en la **composición**, la parte depende del ciclo de vida del todo.

---

## 3. Ejemplo Conceptual (Estructura de Clases)

```text
+------------------+          1..*          +------------------+
|     Curso        |------------------------|     Unidad       |
+------------------+                        +------------------+
| - codigo: String |                        | - titulo: String |
| - nombre: String |                        | - horas: Int     |
+------------------+                        +------------------+
| + agregarUnidad()|                        | + esCompleta()   |
+------------------+                        +------------------+
```

---

## 4. Cuadro Comparativo: Herencia vs. Composición

| Criterio | Herencia (`es un`) | Composición (`tiene un` fuerte) |
| :--- | :--- | :--- |
| **Acoplamiento** | Más estrecho; cambios en la clase base afectan subclases. | Más flexible; facilita reutilización y cambio de piezas. |
| **Reutilización** | Especialización de un tipo general. | Ensamblaje de componentes especializados. |
| **Ciclo de Vida** | Comparten definición de tipo desde su creación. | El componente vive ligado a la existencia del contenedor. |

---

## 5. Análisis de Complejidad

* **Impacto en Mantenimiento:** Diseñar con claridad las fronteras entre clases y sus dependencias en StarUML previene acoplamientos excesivos y facilita probar o modificar módulos de forma aislada.

---

## 6. Conclusión
El dominio del diagrama de clases en StarUML conecta el análisis del dominio del problema con una arquitectura orientada a objetos ordenada en Python o Dart.