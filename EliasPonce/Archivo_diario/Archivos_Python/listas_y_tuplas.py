# Investigación Exhaustiva: Listas y Tuplas en Python

En Python, las **listas** y las **tuplas** son las estructuras de datos secuenciales más utilizadas para almacenar colecciones de elementos. Aunque comparten similitudes en su sintaxis de indexación, difieren fundamentalmente en su **mutabilidad**, **rendimiento** y **propósito de diseño**.

---

## 1. Listas (`list`)

Una lista es una colección de elementos **ordenada, mutable (modificable) y que permite duplicados**. Se definen utilizando corchetes `[]` o el constructor `list()`.

### Características Principales
- **Mutables:** Se pueden añadir, eliminar o modificar elementos después de su creación.
- **Dinámicas:** Su tamaño cambia automáticamente a medida que se agregan o quitan elementos.
- **Heterogéneas:** Pueden contener elementos de diferentes tipos de datos simultáneamente.

### Métodos y Funciones de las Listas

A continuación se detallan todas las funciones y métodos integrados para manipular listas:

| Método / Función | Descripción | Ejemplo de Código |
| :--- | :--- | :--- |
| `append(x)` | Añade un elemento `x` al final de la lista. | `lista.append(4)` |
| `extend(iterable)` | Añade todos los elementos de un iterable al final. | `lista.extend([5, 6])` |
| `insert(i, x)` | Inserta el elemento `x` en la posición de índice `i`. | `lista.insert(0, 'inicio')` |
| `remove(x)` | Elimina la primera aparición del elemento `x`. | `lista.remove('inicio')` |
| `pop([i])` | Elimina y devuelve el elemento en el índice `i` (por defecto el último). | `elemento = lista.pop()` |
| `clear()` | Elimina todos los elementos de la lista, dejándola vacía. | `lista.clear()` |
| `index(x[, s[, e]])`| Devuelve el índice de la primera aparición de `x`. | `idx = lista.index(5)` |
| `count(x)` | Devuelve el número de veces que `x` aparece en la lista. | `repeticiones = lista.count(2)` |
| `sort(key=None, reverse=False)` | Ordena los elementos de la lista *in-place* (modifica la original). | `lista.sort(reverse=True)` |
| `reverse()` | Invierte el orden de los elementos *in-place*. | `lista.reverse()` |
| `copy()` | Devuelve una copia superficial (*shallow copy*) de la lista. | `nueva_lista = lista.copy()` |

### Ejemplo Práctico de Listas

```python
# Creación y manipulación de una lista
frutas = ["manzana", "banana", "cereza"]

# Añadir elementos
frutas.append("naranja")
frutas.insert(1, "uva")

# Modificar un elemento
frutas[0] = "arándano"

# Eliminar elementos
eliminada = frutas.pop() # Elimina "naranja"

print("Lista final:", frutas)
# Resultado: ['arándano', 'uva', 'banana', 'cereza']
```

---

## 2. Tuplas (`tuple`)

Una tupla es una colección de elementos **ordenada, inmutable (no modificable) y que permite duplicados**. Se definen utilizando paréntesis `()` o el constructor `tuple()`.

### Características Principales
- **Inmutables:** Una vez creada, no se pueden añadir, eliminar ni cambiar sus elementos.
- **Estructura fija:** Su tamaño y contenido son permanentes en memoria, lo que las hace más seguras para datos que no deben cambiar.
- **Acceso rápido:** Son ligeramente más rápidas en rendimiento que las listas.

### Métodos y Funciones de las Tuplas

Dado que las tuplas son inmutables, **no poseen métodos para modificar su contenido** (como `append` o `remove`). Solo tienen dos métodos integrados:

| Método / Función | Descripción | Ejemplo de Código |
| :--- | :--- | :--- |
| `count(x)` | Devuelve el número de veces que `x` aparece en la tupla. | `tupla.count(10)` |
| `index(x[, s[, e]])`| Devuelve el índice de la primera aparición de `x`. | `idx = tupla.index(10)` |

### Ejemplo Práctico de Tuplas

```python
# Creación de una tupla
coordenadas = (40.7128, -74.0060)

# Intento de modificación (Esto lanzará un TypeError)
# coordenadas[0] = 50.0 

# Uso de métodos disponibles
valores = (1, 2, 3, 2, 4, 2)
print("El número 2 aparece:", valores.count(2), "veces") # Resultado: 3
print("El número 3 está en el índice:", valores.index(3)) # Resultado: 2
```

---

## 3. Funciones Compartidas (Built-in Functions)

Python ofrece funciones nativas que operan tanto en listas como en tuplas (y en cualquier otro iterable):

*   `len(iterable)`: Devuelve la cantidad total de elementos.
*   `max(iterable)`: Devuelve el elemento con el valor máximo.
*   `min(iterable)`: Devuelve el elemento con el valor mínimo.
*   `sum(iterable)`: Suma todos los elementos (solo si son numéricos).
*   `sorted(iterable, ...)`: Devuelve una **nueva lista** ordenada con los elementos del iterable original (sin modificar el original si es una lista, y permitiendo ordenar tuplas).
*   `tuple(iterable)` / `list(iterable)`: Funciones de conversión de tipo (*casting*).

---

## 4. Tabla Comparativa: Listas vs. Tuplas

| Característica | Listas (`list`) | Tuplas (`tuple`) |
| :--- | :--- | :--- |
| **Sintaxis** | Corchetes `[1, 2, 3]` | Paréntesis `(1, 2, 3)` |
| **Mutabilidad** | **Mutable** (se puede modificar) | **Inmutable** (no se puede modificar) |
| **Tamaño en Memoria**| Mayor (reserva espacio para crecer) | Menor (optimizado y fijo) |
| **Rendimiento** | Más lenta en creación e iteración | Más rápida en creación e iteración |
| **Uso Principal** | Colecciones homogéneas de tamaño variable | Datos heterogéneos fijos, llaves de diccionarios |

---

## 5. ¿Cuándo usar cuál?

1.  **Usa Listas cuando:**
    *   Necesites una colección de datos que cambie con el tiempo (por ejemplo, una lista de compras, usuarios activos, resultados de una base de datos).
    *   Requieras ordenar, barajar o filtrar los datos constantemente.

2.  **Usa Tuplas cuando:**
    *   Tengas datos constantes que no deban cambiar durante la ejecución del programa (por ejemplo, los días de la semana, configuraciones, coordenadas geográficas).
    *   Necesites usar la colección como **llave (*key*) en un diccionario**, ya que las listas no son *hashables* por ser mutables.
    *   Quieras proteger tus datos contra modificaciones accidentales (*Read-Only data*).
