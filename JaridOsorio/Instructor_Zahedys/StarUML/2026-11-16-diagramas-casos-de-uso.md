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
                      
```

---

## 4. Cuadro Comparativo: Casos de Uso vs. Historias de Usuario

| Criterio | Diagrama de Casos de Uso (UML) | Historias de Usuario |
| :--- | :--- | :--- |
| **Formato** | Gráfico con flujos principales, alternos y de excepción. | Breve enunciado textual centrado en valor y criterio de aceptación. |
| **Enfoque** | Alcance funcional y límites del sistema desde el exterior. | Priorización ágil y conversación continua con el cliente. |
| **Detalle de Pasos** | Permite documentar secuencias de interacción claras. | Mantiene el detalle ligero hasta la planificación del sprint. |

---

## 5. Análisis de Complejidad

* **Impacto en el Diseño:** Modelar los casos de uso en StarUML antes de programar reduce la ambigüedad de requisitos y evita construir funcionalidades fuera del alcance, disminuyendo retrabajos costosos en fases posteriores.

---

## 6. Conclusión
Dominar los diagramas de casos de uso en StarUML brinda una visión clara de lo que el sistema debe hacer desde la perspectiva del usuario, sirviendo como puente sólido hacia el diseño técnico.