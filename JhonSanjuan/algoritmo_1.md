s
Vectores en PSeInt

En programación, un vector es una estructura de datos que almacena varios valores del mismo tipo bajo un solo nombre, organizados en posiciones (índices). En PSeInt se le conoce como arreglo o vector unidimensional.

Declaración de un vector

En PSeInt, los vectores se declaran indicando el tamaño entre corchetes o paréntesis, dependiendo de la versión:

Algoritmo EjemploVector
Definir numeros Como Entero
Dimension numeros[10]
FinAlgoritmo
Dimension reserva el espacio en memoria.
numeros[10] crea un vector de 10 posiciones (índices de 1 a 10, ya que PSeInt suele iniciar en 1).
Cargar datos en un vector
Algoritmo CargarVector
Definir numeros Como Entero
Definir i Como Entero
Dimension numeros[5]

Operaciones comunes con vectores
Sumar todos los elementos
Definir suma Como Entero
suma <- 0

Para i = 1 Hasta 5 Con Paso 1
    suma <- suma + numeros[i]
FinPara

Escribir "La suma es: ", suma 
Buscar el mayor valor
Definir mayor Como Entero
mayor <- numeros[1]

Para i = 2 Hasta 5 Con Paso 1
    Si numeros[i] > mayor Entonces
        mayor <- numeros[i]
    FinSi
FinPara

Escribir "El mayor valor es: ", mayor