
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