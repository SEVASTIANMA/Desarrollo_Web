### Estrategia de Validación de Entradas en Programación Defensiva

La estrategia de validación de entradas se divide en tres capas principales:

1. **Validación de Tipo de Dato:** 
   * Comprobar que el valor recibido coincida exactamente con la estructura esperada (por ejemplo, asegurar que un campo de edad sea estrictamente un número entero positivo o que un identificador sea un valor alfanumérico).

2. **Restricción de Longitud (Límites):** 
   * Definir un límite mínimo y máximo de caracteres para evitar ataques de denegación de servicio (DoS) por agotamiento de memoria o desbordamiento de búfer (*buffer overflow*).

3. **Verificación de Formato (Expresiones Regulares y Listas Blancas):** 
   * Aplicar reglas estrictas que permitan únicamente los caracteres válidos. Es preferible usar un enfoque de **lista blanca** (permitir solo lo conocido como seguro) en lugar de una lista negra (bloquear caracteres específicos).

---

### Ejemplo de Implementación Lógica (Pseudocódigo / Validación en Backend)


FUNCION validarNombreUsuario(entrada):
    // 1. Verificar que no esté vacío
    SI entrada ES NULO O longitud(entrada) == 0 ENTONCES:
        RETORNAR Falso, "El campo no puede estar vacío"
    
    // 2. Verificar longitud máxima y mínima
    SI longitud(entrada) < 3 O longitud(entrada) > 20 ENTONCES:
        RETORNAR Falso, "El nombre debe tener entre 3 y 20 caracteres"
    
    // 3. Verificar formato (Solo letras y números, sin caracteres especiales)
    SI NO coincideConPatron(entrada, "^[a-zA-Z0-9]+$") ENTONCES:
        RETORNAR Falso, "El formato contiene caracteres no permitidos"
        
    RETORNAR Verdadero, "Entrada válida" 
    ### Puntos Clave para Cumplir el Criterio de Aceptación


**Validar siempre en el servidor (Backend):** Aunque la validación en el cliente (HTML/JavaScript) mejora la experiencia de usuario, un atacante puede omitirla fácilmente. La validación del servidor es la única que garantiza seguridad real.
* **Fallo seguro:** Si una entrada no cumple exactamente con las reglas definidas, el sistema debe rechazar el procesamiento por defecto y registrar el evento en los logs de auditoría sin exponer detalles técnicos al usuario.

### Estrategia de Sanitización

1. **Codificación de Entidades HTML (*HTML Entity Encoding*):**
   * Transforma caracteres especiales con significado en HTML a sus equivalentes seguros antes de renderizarlos en el navegador. Esto evita la vulnerabilidad de **Cross-Site Scripting (XSS)**.
   * *Ejemplo de conversión:*
     * `<` se convierte en `&lt;`
     * `>` se convierte en `&gt;`
     * `"` se convierte en `&quot;`
     * `'` se convierte en `&#x27;`
     * `&` se convierte en `&amp;`

2. **Limpieza o Eliminación de Etiquetas (*HTML Stripping*):**
   * Remueve por completo etiquetas potencialmente peligrosas (como `<script>`, `<iframe>`, `onload=`, `onerror=`) si el campo no requiere formato HTML.

3. **Uso de Librerías Especializadas:**
   * Evitar el uso de expresiones regulares caseras para limpiar HTML complejo. Es recomendable utilizar componentes probados por la comunidad (como DOMPurify en JavaScript o Bleach en Python).

---

### Ejemplo de Implementación Lógica (Pseudocódigo / Backend)


FUNCION sanitizarParaHTML(cadenaEntrada):
    // Si la entrada no es texto o está vacía, retornar cadena vacía
    SI cadenaEntrada ES NULO O longitud(cadenaEntrada) == 0 ENTONCES:
        RETORNAR ""

     Reemplazar caracteres especiales por entidades HTML seguras
    textoSeguro = reemplazar(cadenaEntrada, "&", "&amp;")
    textoSeguro = reemplazar(textoSeguro, "<", "&lt;")
    textoSeguro = reemplazar(textoSeguro, ">", "&gt;")
    textoSeguro = reemplazar(textoSeguro, '"', "&quot;")
    textoSeguro = reemplazar(textoSeguro, "'", "&#x27;")

    RETORNAR textoSeguro

  

1. **Separación de Lógica y Datos:**
   * La estructura de la consulta SQL se envía primero al motor de la base de datos para ser compilada.
   * Los valores ingresados por el usuario se envían por separado como parámetros neutros, evitando la interpretación de caracteres especiales (como `' OR '1'='1`).

2. **Prohibición de Concatenación Directa:**
   * Nunca se deben construir consultas uniendo cadenas mediante operadores de texto (por ejemplo: `"SELECT * FROM usuarios WHERE id = " + inputUsuario`).

---

