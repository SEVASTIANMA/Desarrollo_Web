# visual basic 
Sub programa()

    A = InputBox("Digite tu edad")
    Nombre = InputBox("Digita tu nombre")

    MsgBox (Nombre & " tiene " & A & " Años")

End Sub
# dartpad
void main() {

int edad = 23; String nombre = "Jarid Osorio";

print(nombre + " tiene " + edad.toString() + " años de edad."); } 

# java
import java.util.Scanner;

public class NombreApellido { public static void main(String[] args) { // Crear el objeto Scanner para leer la entrada del usuario Scanner scanner = new Scanner(System.in);

    System.out.print("Digita tu nombre: ");
    String nombre = scanner.nextLine();

    System.out.print("Digita tu apellido: ");
    String apellido = scanner.nextLine();

    // Mostrar el resultado combinado
    System.out.println("Tu nombre completo es: " + nombre + " " + apellido);

    // Cerrar el scanner para liberar recursos
    scanner.close();
}
}

# Programa secuencial en Java

El programa se ejecuta de manera **secuencial en la consola**, leyendo los datos ingresados por teclado paso a paso hasta mostrar el resultado final combinado.

## Flujo de ejecución

### Inicio

La aplicación arranca desde el método principal (`main`) y crea el objeto encargado de leer el teclado.

### Captura de nombre

El programa imprime la solicitud en pantalla y se detiene a la espera de que el usuario escriba su nombre y presione la tecla **Enter**.

### Captura de apellido

Se repite la acción anterior, pidiendo el apellido.

### Resultado y cierre

Se unen ambas variables con un espacio de separación, se imprime el mensaje completo y se liberan los recursos del sistema.

## Explicación de los componentes

### `import java.util.Scanner;`

Incorpora la clase `Scanner` desde la biblioteca estándar de Java. Permite que el programa pueda interactuar con el exterior leyendo datos desde la consola.

### `Scanner scanner = new Scanner(System.in);`

Instancia un objeto de tipo `Scanner` nombrado `scanner`. El argumento `System.in` configura al lector para que tome los datos ingresados a través del teclado.

### `System.out.print`

Muestra un mensaje en pantalla sin hacer un salto de línea al final. Esto ubica el cursor del usuario exactamente al lado del texto guía.

### `scanner.nextLine()`

Lee todo lo que el usuario escribe hasta que presiona **Enter**. Se utiliza este método (en lugar de `next()`) para asegurar que se capturen correctamente nombres o apellidos compuestos por varias palabras.

### `System.out.println`

Imprime una línea de texto en la consola y agrega un salto de línea automático al finalizar.

### `scanner.close()`

Cierra el canal de lectura del escáner para evitar fugas de memoria o advertencias de recursos abiertos una vez que ya no se requieren más datos.

