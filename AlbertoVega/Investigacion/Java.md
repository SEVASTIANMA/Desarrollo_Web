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

