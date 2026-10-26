
# HTML: La Estructura de la Página

HTML funciona mediante **etiquetas** (tags) que envuelven el contenido para indicarle al navegador qué tipo de elemento es. Casi todas las etiquetas tienen una apertura `<etiqueta>` y un cierre `</etiqueta>`.

## Estructura Base

Toda página web necesita un esqueleto inicial para funcionar correctamente:

- `<!DOCTYPE html>`: Declara que el documento es HTML5.
- `<html>`: El contenedor principal de toda la página.
- `<head>`: Contiene metadatos, el título de la pestaña y enlaces a estilos. No es visible en la página.
- `<body>`: Contiene todo el contenido visible (textos, imágenes, videos).

## Textos y Jerarquía

- `<h1>` a `<h6>`: Definen los encabezados. `<h1>` es el título principal (solo debe haber uno por página) y `<h6>` es el de menor importancia.
- `<p>`: Define un párrafo de texto estándar.
- `<strong>` y `<em>`: Aplican negrita (importancia fuerte) y cursiva (énfasis) al texto respectivamente.

## Multimedia y Navegación

- `<a href="url">`: Crea un enlace o hipervínculo hacia otra página. El atributo `href` indica el destino.
- `<img src="imagen.jpg" alt="Descripción">`: Inserta una imagen. No tiene etiqueta de cierre. El atributo `src` indica la ruta del archivo y `alt` el texto alternativo si la imagen no carga.

## Agrupación y Listas

- `<div>`: Un contenedor genérico en bloque. Se usa para agrupar elementos y aplicarles estilos estructurales.
- `<span>`: Un contenedor genérico en línea. Sirve para aplicar estilo a una parte específica de un texto.
- `<ul>` y `<ol>`: Crean listas desordenadas (viñetas) y ordenadas (números). Cada elemento de la lista debe ir dentro de una etiqueta `<li>`.

---


# CSS: El Diseño y la Apariencia

CSS utiliza **reglas** que consisten en un **selector** (qué elemento modificar) y un bloque de **declaraciones** (qué propiedades cambiar).

## Selectores Básicos

- **Por etiqueta:** Modifica todas las etiquetas de ese tipo. Ejemplo: `p { ... }` afecta a todos los párrafos.
- **Por clase (`.`):** Modifica elementos que compartan un atributo `class` específico. Ejemplo: `.boton-rojo { ... }`. Es el método más utilizado porque es reutilizable.
- **Por ID (`#`):** Modifica un elemento único con un atributo `id` específico. Ejemplo: `#menu-principal { ... }`.

## Propiedades Esenciales

- `color`: Cambia el color del texto (ej. `color: blue;` o `color: #ff0000;`).
- `background-color`: Define el color de fondo de un elemento.
- `font-family`: Establece el tipo de letra (ej. `font-family: Arial, sans-serif;`).
- `font-size`: Modifica el tamaño del texto (ej. `font-size: 16px;`).
- `text-align`: Alinea el texto (ej. `left`, `center`, `right`).

## El Modelo de Caja (Box Model)

Todo en la web es una caja rectangular. Estas propiedades controlan el espacio alrededor y dentro de esas cajas:

- `margin`: Espacio invisible *fuera* del borde del elemento (separa el elemento de otros).
- `padding`: Espacio *dentro* del elemento, entre el contenido y su borde.
- `border`: Una línea que rodea la caja (ej. `border: 1px solid black;`).
- `width` y `height`: Definen el ancho y el alto de la caja.

---

## Ejemplo Integrado

Aquí tienes cómo se ven ambos lenguajes trabajando juntos. El CSS está integrado en la sección `<head>` usando la etiqueta `<style>`: