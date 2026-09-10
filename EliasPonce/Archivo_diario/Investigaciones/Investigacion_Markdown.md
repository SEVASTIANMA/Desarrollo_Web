# Investigación: Markdown (Parte 1)

**Markdown** es un lenguaje de marcado ligero creado por John Gruber y Aaron Swartz en 2004. Su objetivo principal es ofrecer la **máxima legibilidad y facilidad de escritura**, permitiendo que un texto con formato web sea fácil de leer en su forma de código fuente, sin etiquetas complejas como las de HTML.

---

## Principales Características

* **Sintaxis ultra sencilla:** Utiliza caracteres comunes del teclado (como asteriscos, almohadillas y guiones) para dar formato al texto.
* **Legibilidad:** El texto sin procesar sigue siendo perfectamente legible para los humanos.
* **Conversión a HTML:** Se transforma de forma automática y transparente en código HTML válido para su visualización en navegadores.
* **Independencia de plataforma:** Al ser texto plano, se puede escribir y leer en cualquier sistema operativo, editor de texto o dispositivo.
* **Estándar en el desarrollo:** Es el formato nativo para la documentación en plataformas como GitHub, GitLab, Stack Overflow, Reddit, Discord y editores de código modernos como Visual Studio y VS Code.
## 
 Sintaxis Básica de Markdown

A continuación se detallan los elementos fundamentales para estructurar y dar formato a tus documentos.

### 1. Títulos (Encabezados)
Se estructuran utilizando el símbolo de almohadilla `#`. El número de símbolos determina el nivel del título (del 1 al 6).

# Título 1 (H1)
## Título 2 (H2)
### Título 3 (H3)
#### Título 4 (H4)

### 2. Formato de Texto
Permite dar énfasis visual a palabras o frases completas.

Este texto está en **negrita**.
Este texto está en *cursiva*.
Este texto está ~~tachado~~.

### 3. Listas
Puedes crear estructuras ordenadas o desordenadas de forma rápida.

* **Listas desordenadas:** Usa asteriscos `*` o guiones `-`.
  * Elemento A
  * Elemento B
* **Listas ordenadas:** Usa números seguidos de un punto.
  1. Primer paso
  2. Segundo paso

### 4. Enlaces e Imágenes
Las estructuras son similares, pero las imágenes llevan un signo de exclamación al inicio.

* [Visita Google](https://google.com)
* ![Texto alternativo](https://placeholder.com)

### 5. Bloques de Código
Ideal para resaltar fragmentos de programación o comandos de terminal.

* **Código en línea:** Usa una comilla invertida para `código en línea`.
* **Bloques de código:** Usa tres comillas invertidas indicando el lenguaje para el resaltado de sintaxis:

```javascript
function saludar() {
    console.log("¡Hola, mundo!");
}
```

### 6. Citas de Texto y Líneas Divisorias
Se utiliza el símbolo mayor que `>` para citas y tres guiones para separar secciones.

> "La simplicidad es la máxima sofisticación." — Leonardo da Vinci

---
