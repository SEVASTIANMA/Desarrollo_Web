# Investigación: Fundamentos y Buenas Prácticas en Control de Versiones con Git

## 1. Definición
**Git** es un sistema de control de versiones distribuido diseñado para rastrear cambios en el código fuente durante el desarrollo de software. Permite a los desarrolladores mantener un historial preciso, trabajar en ramas paralelas y sincronizar repositorios de forma segura en plataformas como GitHub.

---

## 2. Lógica del Flujo de Trabajo
El flujo estándar opera en tres estados principales:
1. **Working Directory (Directorio de Trabajo):** Donde se modifican los archivos localmente.
2. **Staging Area (Área de Preparación):** Espacio donde se seleccionan y preparan los cambios listos para el commit (`git add`).
3. **Repository (Repositorio Local):** Historial permanente de commits guardados (`git commit`).

---

## 3. Ejemplo de Comandos Esenciales

```bash
# Inicializar o clonar repositorio
git status
git add .
git commit -m "docs: actualizar actividades diarias"
git push origin main

```

---

## 4. Cuadro Comparativo: Control Manual vs. Git

| Criterio | Copias de Respaldo Manuales (Carpeta .zip) | Control de Versiones con Git |
| :--- | :--- | :--- |
| **Historial** | Confuso, nombres repetidos (`proyecto_v1`, `final_final`). | Lineal, detallado, con autor, fecha y mensaje descriptivo. |
| **Trabajo en Equipo** | Alto riesgo de sobreescribir archivos de compañeros. | Sincronización limpia, fusiones automáticas y resolución de conflictos. |

---

## 5. Análisis de Complejidad

* **Eficiencia Operativa:** Git utiliza algoritmos basados en grafos acíclicos dirigidos y compresión de diferencias (*deltas*), lo que optimiza el espacio en disco y acelera la recuperación de versiones anteriores en comparación con almacenar copias completas de proyectos enteros.

---

## 6. Conclusión
El dominio de Git y GitHub Desktop es una competencia indispensable en el programa ADSO, garantizando la trazabilidad, seguridad y profesionalismo en la entrega de productos de software.