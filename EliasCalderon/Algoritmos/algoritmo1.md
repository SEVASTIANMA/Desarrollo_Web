### Configuración Inicial
* **Número secreto:** El juego genera un valor aleatorio (n) entre 1 y 100.
* **Contador:** Inicializa la variable intentos en 0 para registrar las jugadas.

### Bucle Principal (Mientras)
El programa solicita un número al usuario, lo compara con el número secreto y repite el ciclo hasta que el usuario acierta:
* **Si el número es mayor:** Pide probar con uno menor.
* **Si el número es menor:** Pide probar con uno mayor.
* **Registro:** Suma 1 al contador de intentos en cada ciclo fallido.

### Evaluación Final
Al adivinar el número, el programa muestra un mensaje de éxito y califica el desempeño según los intentos:
* **Menos de 10 intentos:** "Lo hiciste muy bien"
* **Entre 10 y 15 intentos:** "Lo pudiste hacer mejor"
* **Más de 15 intentos:** Muestra un mensaje de frustración ("No lo intestes mas mongolo").


Algoritmo Adivinanza2
	intentos <- 0
	n = aleatorio(1,100)
	Definir num Como Entero
	Escribir 'Digite un numero'
	Leer num
	Mientras num <> n Hacer
		si num > n Entonces
			Escribir 'Prueba con un numero menor'
		SiNo
			Escribir 'Prueba con un numero mayor'
		FinSi
		Escribir 'sigue intentando'
		Leer num
		intentos= intentos + 1
	FinMientras
	Escribir '==============================='
	si intentos < 10 Entonces
		Escribir '   Lo hiciste muy bien'
	SiNo
		si intentos <= 15 Entonces
			Escribir '  Lo pudiste hacer mejor'
		SiNo
			si intentos > 15 Entonces
				Escribir '  No lo intestes mas mongolo'
			FinSi
		FinSi
	FinSi
	Escribir '  Lo has logrado adivinar!!!!!!'
	Escribir '  Numero de intentos: ' intentos
	Escribir '==============================='
FinAlgoritmo
