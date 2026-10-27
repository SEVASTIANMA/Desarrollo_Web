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
# Guía Avanzada de Pull Requests en GitHub - Parte 2: Flujo Técnico y Conflictos

Para crear y gestionar un Pull Request de forma profesional, se debe seguir rigurosamente el flujo de trabajo de Git (*Git Flow* o *GitHub Flow*), asegurando la estabilidad del repositorio principal.

---

## 3. ¿Cómo se hace un Pull Request? (Paso a Paso)

### Paso 1: Aislar el trabajo en una rama local
Nunca modifiques la rama principal (`main` o `master`) directamente. Crea una rama secundaria específica para tu tarea:
```bash
git checkout -b feature/recuperar-contrasena
```

### Paso 2: Desarrollar y guardar los cambios
Escribe tu código, realiza pruebas locales y registra tus avances con commits claros y descriptivos:
```bash
git add .
git commit -m "feat: agrega validación de correo en formulario de recuperación"
```

### Paso 3: Publicar la rama en GitHub
Sube tu rama local al servidor remoto para que GitHub tenga constancia de tus modificaciones:
```bash
git push origin feature/recuperar-contrasena
```

### Paso 4: Abrir el PR en la plataforma
1. Ve a tu repositorio en **GitHub**. Un banner amarillo te sugerirá hacer clic en **"Compare & pull request"**.
2. Redacta un título claro y una descripción detallada.
3. En el panel derecho, asigna a tus compañeros de equipo en la sección **Reviewers**.
4. Haz clic en el botón verde **Create pull request**.

---

## 4. El Gran Obstáculo: ¿Qué es un Conflicto de Código y cómo se resuelve?

Un **conflicto de merge** ocurre cuando dos desarrolladores modifican las mismas líneas de un mismo archivo en ramas distintas, y Git no puede decidir automáticamente qué versión conservar.

*   **Cómo se ve:** GitHub bloqueará el botón de integración y mostrará el mensaje *"This branch has conflicts that must be resolved"*.
*   **Cómo resolverlo de forma segura (Localmente):**
    1. Regresa a tu rama local: `git checkout feature/recuperar-contrasena`
    2. Trae los cambios más recientes de la rama principal: `git pull origin main`
    3. Abre los archivos conflictivos en tu editor de código. Verás marcas como `<<<<<<< HEAD` y `>>>>>>>`.
    4. Decide con qué código quedarte, borra las marcas de Git, guarda el archivo, haz un nuevo commit y súbelo (`git push`). El PR se actualizará automáticamente en GitHub.
# Guía Avanzada de Pull Requests en GitHub - Parte 3: Automatización y Calidad

Un Pull Request exitoso no termina cuando el código funciona; concluye cuando se integra de manera limpia y automatizada, respetando las buenas prácticas de la industria.

---

## 5. El Rol de CI/CD (Integración Continua) en un PR

En entornos profesionales, los PRs están conectados a sistemas de **CI/CD** (como GitHub Actions). Al abrir o actualizar un PR, se ejecutan automáticamente los siguientes controles:

*   **Linters:** Herramientas que analizan el código para asegurar que cumpla con las reglas de estilo y formato del equipo.
*   **Pruebas Unitarias e Integrales (Tests):** Scripts que verifican que los cambios introducidos no rompan ninguna funcionalidad antigua.
*   **Análisis de Seguridad:** Escáneres que buscan vulnerabilidades o contraseñas expuestas accidentalmente en el código.

Si alguna de estas pruebas falla, el PR mostrará un estado en rojo y, por lo general, se bloqueará la integración hasta que el desarrollador solucione las alertas.

---

## 6. Los Tres Tipos de Merge (Cierre de un PR)

Cuando el código es aprobado y las pruebas pasan, el PR está listo para fusionarse. GitHub ofrece tres formas principales de hacerlo:

*   **Create a Merge Commit:** Fusiona todos los commits de tu rama en la rama principal, manteniendo el historial completo intacto. Es el método por defecto.
*   **Squash and Merge:** Comprime todos tus commits individuales en **uno solo**. Es ideal para mantener el historial de la rama principal limpio y fácil de leer.
*   **Rebase and Merge:** Aplica tus commits uno por uno directamente encima de la rama principal. Conserva un historial lineal sin crear un commit de fusión intermedio.

---

## 7. Checklist de Buenas Prácticas para el Éxito

*   **PRs Atómicos (Pequeños):** Limita tus PRs a un solo propósito. Es preferible revisar tres PRs de 40 líneas que uno solo de 1,200 líneas.
*   **Usa Plantillas (Templates):** Configura un archivo `.github/pull_request_template.md` para estandarizar la información que debe llenar el equipo al abrir un PR.
*   **Autorevisión:** Sé el primero en revisar tu PR en la pestaña *Files Changed*. Elimina comentarios basura (`console.log`, `TODOs` olvidados) antes de pedir tiempo a tus compañeros.
