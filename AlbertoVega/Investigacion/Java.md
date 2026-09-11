# Java

### Código en Java

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("¿Cuántos años tienes?: ");
        String a = scanner.nextLine();
        
        System.out.println("Tienes " + a + " años");
        
        scanner.close();
    }
}
```

---

### Explicación línea por línea

`import java.util.Scanner;`  
Importa la herramienta `Scanner`, que es la biblioteca necesaria para leer lo que el usuario escribe por teclado (el equivalente al `InputBox` en VBA).

`public class Main {`  
Define la clase principal. En Java, todo el código debe estar dentro de una clase.

`public static void main(String[] args) {`  
Es el punto de entrada del programa (el equivalente a `void main()` en Dart o `Sub` en VBA).

`Scanner scanner = new Scanner(System.in);`  
Crea e inicializa el objeto `scanner` configurado para escuchar la entrada del sistema (`System.in` / consola).

`System.out.print("¿Cuántos años tienes?: ");`  
Muestra el mensaje pidiendo el dato. Se usa `print` para que el usuario escriba al lado de la pregunta.

`String a = scanner.nextLine();`  
**Lectura:** El programa espera a que el usuario escriba y presione Enter. `scanner.nextLine()` toma la entrada como texto y la guarda en la variable `a`.

`System.out.println("Tienes " + a + " años");`  
Muestra el resultado aplicando **concatenación de cadenas** con el operador `+` para pegar el texto con la variable `a`.

`scanner.close();`  
Cierra la lectura del teclado para liberar recursos de memoria del sistema.

`}`  
Cierran el cuerpo del método `main` y de la clase `Main`.