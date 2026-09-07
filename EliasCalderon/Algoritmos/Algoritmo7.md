# Explicación del Algoritmo: Adivinanzacorta

Este algoritmo es un juego interactivo de adivinanza numérica. El objetivo principal es que el usuario descubra un número oculto generado al azar por la computadora en la menor cantidad de intentos posible.

---

## Estructura y Funcionamiento Paso a Paso

1. **Configuración Inicial:**
   * `intentos <- 0`: Se inicializa un contador en cero para registrar cuántas veces ha jugado el usuario.
   * `secret = Aleatorio(1,100)`: El sistema genera un número al azar entre el 1 y el 100 y lo guarda como el número secreto a adivinar.

2. **El Bucle de Juego (Repetir ... Hasta Que):**
   * El algoritmo entra en un ciclo que se ejecutará de forma obligatoria al menos una vez, y se repetirá continuamente hasta que se cumpla la condición de salida.
   * `Escribir "Escribe un numero: "` y `leer num`: Muestra un mensaje en pantalla y detiene la ejecución para que el usuario introduzca su número por teclado.

3. **Evaluación y Pistas (Si ... Entonces ... SiNo):**
   * **Condición Mayor:** Si el número del usuario es más alto que el secreto (`num > secret`), el programa le advierte: "Prueba con un numero menor".
   * **Condición Menor/Igual:** Si el número no es mayor, el programa asume por defecto la instrucción del `SiNo` y muestra: "Prueba con un numero mayor".

4. **Conteo de Intentos:**
   * `intentos = intentos + 1`: Al final de cada ronda, el algoritmo suma 1 al contador de intentos, sin importar si el usuario acertó o falló.

5. **Condición de Parada:**
   * `Hasta Que (num = secret)`: El bucle se rompe y finaliza únicamente cuando el número ingresado es exactamente igual al número secreto.

6. **Pantalla de Victoria:**
   * Al salir del bucle, el programa muestra un mensaje de felicitación y despliega en pantalla el número total de intentos que le tomó al jugador ganar.

Algoritmo Adivinanzacorta
	intentos <- 0
	secret = Aleatorio(1,100)
	Repetir
		Escribir "Escribe un numero: "
		leer num
		si num > secret Entonces
			Escribir 'Prueba con un numero menor'
		SiNo
			Escribir 'Prueba con un numero mayor'
		FinSi
		intentos = intentos + 1		
	Hasta Que (num = secret)
	Escribir "Felicitacioneeeeeeees!!!!!!!"
	Escribir "Tu numero de intentos fueron: " intentos	
FinAlgoritmo
