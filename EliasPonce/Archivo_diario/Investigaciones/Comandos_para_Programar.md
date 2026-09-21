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
# Investigación - Parte 2: Diagnóstico, Búsqueda y Monitoreo

Esta sección cubre las herramientas de la línea de comandos enfocadas en la auditoría de código, el monitoreo del rendimiento del sistema y el control de entornos remotos o locales.

---

## 6. `grep` (o `ripgrep`)
### Lenguaje / Entorno compatible
* **Universal.** Herramienta nativa de Unix/Linux (disponible en macOS y Windows mediante WSL o Git Bash). Funciona buscando texto plano dentro de cualquier archivo (.py, .js, .txt, .json, .java, etc.).

### Explicación
Es una herramienta de búsqueda de texto global mediante expresiones regulares. Permite buscar palabras, funciones, variables o patrones específicos dentro de archivos o carpetas enteras desde la terminal.

### Ventajas
* **Auditoría rápida de código:** Encuentra dónde se está usando una función o variable en proyectos masivos sin necesidad de abrir el IDE.
* **Filtrado de logs:** Permite aislar errores específicos dentro de archivos de registro gigantescos combinándolo con otros comandos.

---

## 7. `find`
### Lenguaje / Entorno compatible
* **Universal (Sistemas de archivos).** Comando nativo de sistemas Unix/Linux y macOS. Busca cualquier tipo de extensión o archivo de código en el disco duro.

### Explicación
Busca archivos y directorios en el disco duro basándose en una gran variedad de condiciones: nombre, tipo, tamaño, fecha de modificación o permisos.

### Ventajas
* **Localización exacta:** Encuentra configuraciones o recursos perdidos entre miles de carpetas del sistema de forma inmediata.
* **Acciones en lote:** Se puede combinar con el argumento `-exec` para buscar ciertos archivos (por ejemplo, todos los `.log`) y borrarlos o modificarlos al mismo tiempo.

---

## 8. `ssh` (Secure Shell)
### Lenguaje / Entorno compatible
* **Universal (Administración de servidores).** Utilizado para interactuar con sistemas operativos de servidores (mayormente Linux). Es independiente del código que ejecute el servidor.

### Explicación
Es un protocolo de red que permite a los programadores conectarse y administrar un servidor remoto de forma segura a través de un canal cifrado.

### Ventajas
* **Administración remota:** Permite desplegar aplicaciones, modificar configuraciones o revisar servidores en la nube (AWS, Azure, DigitalOcean) desde tu terminal local.
* **Seguridad:** Cifra todo el tráfico de datos (incluyendo contraseñas), evitando intercepciones.

---

## 9. `top` / `htop`
### Lenguaje / Entorno compatible
* **Universal (Sistemas Operativos).** Herramientas para Linux y macOS (con equivalentes como `tasklist` en Windows). Monitorean procesos de cualquier lenguaje que se esté ejecutando en la máquina local o servidor.

### Explicación
Muestra en tiempo real los procesos que se están ejecutando en el sistema operativo, junto con el consumo de memoria RAM, uso de CPU y almacenamiento. `htop` es una versión mejorada e interactiva visualmente.

### Ventajas
* **Depuración de rendimiento:** Permite identificar si tu código o aplicación local está sufriendo una fuga de memoria (memory leak) o saturando el procesador.
* **Control de procesos:** Permite forzar el cierre de procesos congelados o zombis que bloquean puertos locales.

---

## 10. `lsof -i :[puerto]`
### Lenguaje / Entorno compatible
* **Universal (Redes e infraestructura).** Común en Linux y macOS. Sirve para depurar aplicaciones web de cualquier tipo (servidores Node.js, Django, Ruby on Rails, Spring Boot, etc.) que escuchen en puertos TCP/UDP.

### Explicación
Significa "List Open Files". Usado con la bandera `-i`, muestra qué proceso o aplicación tiene bloqueado un puerto de red específico (por ejemplo, el puerto 8080 o 3000).

### Ventajas
* **Resolución de conflictos:** Resuelve el clásico error `Error: listen EADDRINUSE: address already in use`, permitiéndote encontrar el ID del proceso (PID) que bloquea tu servidor para poder cerrarlo.
