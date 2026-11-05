# Investigación: Paradigmas de Programación (Estructurado vs. Orientado a Objetos)

## 1. Definición
Un **paradigma de programación** es un enfoque o estilo fundamental para estructurar y organizar el código de un sistema de software. Los dos paradigmas más influyentes en el desarrollo moderno son la **Programación Estructurada** y la **Programación Orientada a Objetos (POO)**.

---

## 2. Lógica del Paradigma
1. **Programación Estructurada:** Se basa en secuencias de instrucciones, condicionales y bucles, dividiendo el problema en funciones y procedimientos.
2. **Programación Orientada a Objetos:** Modela el software alrededor de "objetos" reales o abstractos que agrupan datos (atributos) y comportamientos (métodos).

---

## 3. Ejemplo Comparativo en Código

```python
# Estructurado (Funcional)
def calcular_area(base, altura):
    return base * altura

# Orientado a Objetos (POO)
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
``` 

---

## 4. Cuadro Comparativo: Estructurado vs. POO

| Criterio | Programación Estructurada | Programación Orientada a Objetos |
| :--- | :--- | :--- |
| **Enfoque Principal** | Algoritmos y lógica de pasos paso a paso. | Entidades, datos y relaciones entre objetos. |
| **Reutilización** | Mediante funciones y librerías. | Mediante herencia, polimorfismo y encapsulamiento. |
| **Mantenibilidad** | Dificultad alta en proyectos grandes. | Alta escalabilidad y modularidad en proyectos complejos. |

---

## 5. Análisis de Complejidad

* **Impacto en Rendimiento:** La programación estructurada suele tener un menor *overhead* de memoria, mientras que POO agrega abstracción que facilita el trabajo en equipo a costa de un leve consumo adicional de recursos.

---

## 6. Conclusión
Comprender ambos paradigmas permite elegir la herramienta adecuada según el problema: la programación estructurada es ideal para scripts y automatización corta (como en VBA o Python básico), mientras que POO es indispensable para aplicaciones robustas en Python y Dart.

