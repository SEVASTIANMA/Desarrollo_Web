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

