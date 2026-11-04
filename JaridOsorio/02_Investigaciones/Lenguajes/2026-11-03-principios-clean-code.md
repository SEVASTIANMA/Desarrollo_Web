# Investigación: Principios de Código Limpio y Buenas Prácticas de Desarrollo

## 1. Definición
El **Código Limpio (Clean Code)** es una filosofía de desarrollo de software enfocada en escribir código que sea fácil de leer, comprender, mantener y extender por cualquier otro desarrollador del equipo, minimizando la deuda técnica.

---

## 2. Pilares Fundamentales
1. **Nombres Significativos:** Variables y funciones deben revelar su propósito (ej. `diasTranscurridos` en lugar de `d`).
2. **Funciones Pequeñas:** Cada función debe realizar una única tarea y hacerlo bien.
3. **Comentarios Útiles:** El código debe explicarse por sí mismo; los comentarios deben reservarse para explicar decisiones complejas o de negocio.

---

## 3. Ejemplo Conceptual

```python
# Código confuso (Mala práctica)
def calc(d):
    return d * 24 * 60

# Código limpio (Buena práctica)
def convertir_dias_a_minutos(cantidad_dias):
    minutos_en_un_dia = 24 * 60
    return cantidad_dias * minutos_en_un_dia

```

---

## 4. Cuadro Comparativo: Código Desordenado vs. Código Limpio

| Criterio | Código Desordenado ("Spaghetti") | Código Limpio y Estructurado |
| :--- | :--- | :--- |
| **Mantenibilidad** | Extremadamente compleja; un cambio rompe otras partes. | Modular y segura; cambios aislados sin efectos secundarios. |
| **Legibilidad** | Requiere mucho tiempo de análisis e interpretación. | Intuitiva y fluida para cualquier programador. |

---

## 5. Análisis de Complejidad

* **Impacto Estructural:** Aplicar principios de Clean Code no altera directamente la complejidad algorítmica ($O(n)$), pero reduce drásticamente la complejidad cognitiva y el tiempo dedicado a depuración (*debugging*).

---

## 6. Conclusión
Adoptar buenas prácticas de Clean Code desde la etapa formativa en el SENA asegura la creación de software robusto, escalable y profesional alineado con los estándares de la industria tecnológica actual.