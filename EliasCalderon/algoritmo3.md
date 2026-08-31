### Configuración Inicial
* **Variables:** Define la variable total como un número entero.
* **Contador:** Inicializa total en 0 para registrar cuántas personas son menores de edad.
* **Entrada de datos:** Solicita la edad de forma general e ingresa consecutivamente 5 valores independientes (edad1, edad2, edad3, edad4 y edad5).

### Procesamiento y Comparación
El programa evalúa de forma individual la edad de cada una de las 5 personas mediante estructuras condicionales simples:
* **Primera edad:** Si edad1 es menor a 18, suma 1 al contador total.
* **Segunda edad:** Si edad2 es menor a 18, suma 1 al contador total.
* **Tercera edad:** Si edad3 es menor a 18, suma 1 al contador total.
* **Cuarta edad:** Si edad4 es menor a 18, suma 1 al contador total.
* **Quinta edad:** Si edad5 es menor a 18, suma 1 al contador total.

### Evaluación Final
* **Resultado:** Imprime en pantalla el texto "Los menores de edad contabilizados son:" junto con el valor acumulado en la variable total.




Algoritmo eDadPersonas
	Definir total Como Entero
	total <- 0
	Escribir '�Cuantos a�os tienes?'
	Leer edad1
	Leer edad2
	Leer edad3
	Leer edad4
	Leer edad5
	
	si edad1 < 18 Entonces
		total <- total + 1
	FinSi
	
	si edad2 < 18 Entonces
		total <- total + 1
	FinSi
		
	si edad3 < 18 Entonces
		total <- total + 1
	FinSi
	
	si edad4 < 18 Entonces
	 total <- total + 1
	FinSi
	
	si edad5 < 18 Entonces
		total <- total + 1
	FinSi
	
	
	Escribir 'Los menores de edad contabilizados son: ' total
	
	
FinAlgoritmo