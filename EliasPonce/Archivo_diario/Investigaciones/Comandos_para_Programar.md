# Investigación - Parte 1: Control de Versiones y Dependencias

En el desarrollo de software moderno, el dominio de la interfaz de línea de comandos (CLI) es una habilidad fundamental. Optimiza el tiempo, automatiza tareas repetitivas y permite interactuar directamente con el sistema operativo y los servidores.

---

## 1. `git clone`
### Lenguaje / Entorno compatible
* **Universal (Independiente del lenguaje).** Funciona en cualquier sistema operativo (Linux, macOS, Windows) con Git instalado. Es agnóstico al lenguaje (sirve para proyectos en Python, JavaScript, C++, etc.).

### Explicación
Este comando descarga una copia exacta de un repositorio remoto (alojado en plataformas como GitHub, GitLab o Bitbucket) a tu máquina local. No solo descarga los archivos actuales, sino también todo el historial de cambios y ramas del proyecto.

### Ventajas
* **Inicio rápido:** Permite empezar a trabajar en un proyecto existente en cuestión de segundos.
* **Clonación integral:** Descarga todo el historial de control de versiones, permitiéndote explorar ramas antiguas o revisar quién hizo qué cambios.

---

## 2. `git commit --amend`
### Lenguaje / Entorno compatible
* **Universal (Independiente del lenguaje).** Se ejecuta en la terminal sobre cualquier repositorio gestionado con el sistema de control de versiones Git.

### Explicación
Permite modificar el último *commit* realizado en Git. Sirve tanto para corregir un error tipográfico en el mensaje como para añadir archivos que olvidaste incluir en la confirmación original.

### Ventajas
* **Historial limpio:** Evita tener que crear commits innecesarios como "corrección de typo" o "ahora sí con el archivo que faltaba", manteniendo una línea de tiempo profesional.

---

## 3. `npm install` (o `pip install`, `cargo build`, etc.)
### Lenguaje / Entorno compatible
* **Específico del ecosistema del lenguaje.** 
  * `npm install`: JavaScript / TypeScript (Node.js).
  * `pip install`: Python.
  * `cargo build`: Rust.
  * `composer install`: PHP.

### Explicación
Representa al comando de gestión de dependencias de cada lenguaje. Lee el archivo de manifiesto del proyecto (como `package.json`, `requirements.txt` o `Cargo.toml`) y descarga de forma automática todas las librerías necesarias para que el código funcione.

### Ventajas
* **Gestión de librerías:** Evita tener que buscar, descargar y configurar manualmente el código escrito por terceros.
* **Consistencia:** Asegura que todos los desarrolladores del equipo utilicen exactamente las mismas versiones de las librerías.

---

## 4. `docker compose up`
### Lenguaje / Entorno compatible
* **Universal (Cualquier lenguaje contenedorizado).** Funciona en cualquier sistema con Docker instalado. Se usa para empaquetar aplicaciones sin importar si están hechas en Go, Java, Ruby, PHP o sistemas con múltiples lenguajes a la vez.

### Explicación
Pertenece al ecosistema Docker. Este comando define y arranca aplicaciones multi-contenedor basadas en un archivo de configuración `docker-compose.yml`. Levanta bases de datos, servidores web y servicios de backend con una sola línea.

### Ventajas
* **Entornos idénticos:** Garantiza que el proyecto corra exactamente igual en tu máquina, en la de tus compañeros y en el servidor de producción ("en mi máquina sí funciona" deja de ser un problema).
* **Simplicidad:** Configura infraestructuras complejas (como conectar Node.js con PostgreSQL y Redis) al instante.

---

## 5. `curl`
### Lenguaje / Entorno compatible
* **Universal (Protocolos de red).** Es una herramienta nativa de la terminal (Linux/macOS y Windows moderno). Interactúa con servicios web escritos en cualquier lenguaje backend.

### Explicación
Es una herramienta para transferir datos desde o hacia un servidor utilizando diversos protocolos (HTTP, HTTPS, FTP, etc.). Los programadores lo usan principalmente para probar y consumir APIs RESTful o GraphQL.

### Ventajas
* **Prueba de APIs sin interfaz:** Permite enviar peticiones GET, POST, PUT o DELETE rápidamente sin necesidad de abrir herramientas pesadas como Postman.
* **Automatización:** Se puede integrar fácilmente en scripts de Bash para verificar el estado de un servidor o descargar dependencias.
