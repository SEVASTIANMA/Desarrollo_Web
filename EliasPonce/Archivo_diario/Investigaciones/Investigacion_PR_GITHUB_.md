# Guía Avanzada de Pull Requests en GitHub - Parte 1: Fundamentos

Un **Pull Request (PR)** es el pilar del desarrollo de software moderno y colaborativo. Es una funcionalidad nativa de plataformas como GitHub que permite a un desarrollador proponer cambios en el código fuente de un proyecto y solicitar formalmente que un equipo los revise e integre.

---

## 1. ¿Para qué sirve realmente un Pull Request?

El propósito de un PR va mucho más allá de simplemente "mover código". Cumple funciones estratégicas dentro del ciclo de vida del software:

*   **Control de Calidad (Code Review):** Permite que otros ingenieros analicen tu lógica, detecten fallas de seguridad, verifiquen la arquitectura y sugieran optimizaciones antes de que afecte a los usuarios.
*   **Mentoría y Transferencia de Conocimiento:** Es el espacio idóneo para que los desarrolladores juniors aprendan de los seniors a través de la retroalimentación directa en las líneas de código.
*   **Validación Automática:** Actúa como una aduana técnica. Al abrir un PR, se pueden disparar entornos de pruebas que validan si el nuevo código cumple con los estándares del proyecto.
*   **Documentación Viva:** Cada PR se convierte en un registro histórico que explica los motivos de un cambio, facilitando el mantenimiento del software a largo plazo.

---

## 2. Anatomía de un Pull Request en GitHub

Cuando abres un PR en la interfaz web de GitHub, te encontrarás con los siguientes componentes clave:

*   **Cabecera de Ramas:** Muestra la dirección del flujo de código. Indica claramente cuál es la rama de origen (`compare`) y cuál es la rama de destino (`base`), por ejemplo: `base: main` ← `compare: feature/login`.
*   **Pestaña de Conversación (Conversation):** Es el foro principal. Muestra la descripción, el feed de comentarios de los revisores, los resultados de las pruebas automáticas y el estado de aprobación.
*   **Pestaña de Commits:** Un desglose cronológico de cada uno de los guardados parciales que componen tu propuesta de cambio.
*   **Pestaña de Archivos Cambiados (Files Changed):** La vista más importante para los revisores. Muestra un formato *diff* (diferencial) donde las líneas de código eliminadas aparecen en rojo y las nuevas en verde.
