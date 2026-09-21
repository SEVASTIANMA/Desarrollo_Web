### Configuración Inicial
* **Variables:** Define nota1, nota2, nota3 y acumulado como números reales.
* **Entrada de datos:** Solicita e ingresa las calificaciones de los dos primeros cortes (30% cada uno).

### Procesamiento y Cálculo
* **Acumulado:** Multiplica las dos primeras notas por 0.30 y las suma para obtener el puntaje guardado.
* **Nota requerida:** Resta el acumulado al mínimo para aprobar (3.0) y divide el resultado entre 0.40 para calcular cuánta puntuación se necesita en el tercer corte (40%).

### Evaluación Final
El programa analiza el resultado de la tercera nota para determinar la situación académica del estudiante:
* **Nota menor o igual a 0:** Informa que la materia ya está aprobada y se requiere un 0.0.
* **Nota mayor a 5.0:** Advierte que es matemáticamente imposible pasar porque la nota necesaria supera el límite máximo.
* **Nota entre 0.0 y 5.0:** Muestra el valor exacto que se debe obtener en la última calificación para aprobar con 3.0.


Algoritmo CalcularNotaMinima
	Definir nota1, nota2, nota3, acumulado Como Real
	Escribir 'Ingrese la primera nota (30%):'
	Leer nota1
	Escribir 'Ingrese la segunda nota (30%):'
	Leer nota2
	acumulado <- (nota1*0.30)+(nota2*0.30)
	nota3 <- (3.0-acumulado)/0.40
	Si nota3<=0 Entonces
		Escribir '�Ya aprobaste la materia!'
		Escribir 'Necesitas un 0.0 en la tercera nota.'
	SiNo
		Si nota3>5.0 Entonces
			Escribir 'Es matem�ticamente imposible pasar.'
			Escribir 'Requieres una nota de: ', nota3, ' (M�ximo es 5.0)'
		SiNo
			Escribir 'Para pasar con 3.0 necesitas obtener: ', nota3
		FinSi
	FinSi
FinAlgoritmo