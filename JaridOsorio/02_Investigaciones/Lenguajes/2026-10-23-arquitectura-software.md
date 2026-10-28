# Investigación: Arquitectura de Software y Modelos en Capas

## 1. Definición
La **arquitectura de software** es la estructura fundamental de un sistema informático, la cual define cómo interactúan sus componentes, módulos y capas. Facilita la escalabilidad, el mantenimiento y la separación de responsabilidades (por ejemplo, separar la interfaz de usuario de la lógica de negocio y la base de datos).

---

## 2. Lógica del Modelo en Capas
1. **Capa de Presentación (UI):** Interactúa directamente con el usuario (ej. aplicaciones Dart/Flutter o formularios VBA).
2. **Capa de Lógica de Negocio (Backend):** Procesa las reglas, cálculos y validaciones (ej. scripts en Python).
3. **Capa de Datos:** Gestiona el almacenamiento permanente en bases de datos o archivos planos.

---

## 3. Ejemplo Conceptual (Separación de Responsabilidades)

```python
# Capa de Lógica de Negocio
def calcular_descuento(precio, porcentaje):
    return precio - (precio * (porcentaje / 100))

# Capa de Presentación
precio_final = calcular_descuento(100000, 15)
print(f"Precio con descuento aplicado: {precio_final}")
```

---

## 4. Cuadro Comparativo: Arquitectura Monolítica vs. En Capas

| Criterio | Arquitectura Monolítica | Arquitectura en Capas |
| :--- | :--- | :--- |
| **Estructura** | Todo el código se encuentra unido en un solo bloque. | Responsabilidades divididas lógicamente en niveles. |
| **Mantenibilidad** | Compleja y riesgosa a medida que crece el proyecto. | Alta; modificar una capa no afecta directamente a las demás. |
| **Escalabilidad** | Difícil de escalar de forma independiente. | Permite escalar componentes específicos según la demanda. |

---

## 5. Análisis de Complejidad

* **Mantenimiento y Rendimiento:** Aunque la modularidad en capas añade un pequeño nivel de abstracción en llamadas a funciones, reduce drásticamente la complejidad ciclomática general del proyecto y previene errores de acoplamiento.

---

## 6. Conclusión
Comprender la arquitectura en capas es vital en el programa ADSO para diseñar software robusto, limpio y preparado para trabajar en equipo bajo estándares de la industria informática actual.