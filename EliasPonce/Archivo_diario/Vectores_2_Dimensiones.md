# Ejercicio de Vectores 2D - Parte 1: Vector Resultante

Un barco zarpa desde un puerto y realiza un desplazamiento representado por el vector $\vec{A} = (3, 4)$ kilómetros. Posteriormente, realiza un segundo desplazamiento representado por el vector $\vec{B} = (2, -1)$ kilómetros.

Para encontrar la posición final del barco respecto al puerto, calculamos el vector resultante $\vec{R}$ sumando las componentes correspondientes ($x$ con $x$, e $y$ con $y$):

$$\vec{R} = (A_x + B_x, A_y + B_y)$$

### Pasos del cálculo:
* **Componente $x$:** $3 + 2 = 5$
* **Componente $y$:** $4 + (-1) = 3$

**Resultado:** El vector de desplazamiento total es **$\vec{R} = (5, 3)$ kilómetros**.
# Ejercicio de Vectores 2D - Parte 2: Magnitud del Vector

Con el vector resultante anterior $\vec{R} = (5, 3)$, calculamos la distancia total en línea recta desde el puerto hasta la ubicación final del barco. Para ello, aplicamos el **Teorema de Pitágoras**:

$$|\vec{R}| = \sqrt{R_x^2 + R_y^2}$$

### Pasos del cálculo:
1. Elevar las componentes al cuadrado: $5^2 = 25$ y $3^2 = 9$
2. Sumar los resultados: $25 + 9 = 34$
3. Calcular la raíz cuadrada: $\sqrt{34} \approx 5.83$

**Resultado:** La distancia en línea recta desde el puerto es de **$5.83$ kilómetros**.
# Ejercicio de Vectores 2D - Parte 3: Dirección del Vector

Para conocer la orientación exacta del barco, calculamos el ángulo $\theta$ que forma el vector resultante $\vec{R} = (5, 3)$ con respecto al eje positivo de las $x$ (el Este), usando la **tangente inversa**:

$$\theta = \tan^{-1}\left(\frac{R_y}{R_x}\right)$$

### Pasos del cálculo:
1. Dividir la componente $y$ entre la componente $x$: $\frac{3}{5} = 0.6$
2. Aplicar la tangente inversa: $\tan^{-1}(0.6) \approx 30.96^\circ$

**Resultado:** El barco se encuentra en una dirección de **$30.96^\circ$ al noreste**.
