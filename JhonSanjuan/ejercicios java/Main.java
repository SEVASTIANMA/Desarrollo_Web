class Persona {

    String cedula;
    String nombre;

    
    Persona(String cedula) {
        this.cedula = cedula;
    }
}

public class Main {

    public static void main(String[] args) {

        
        Persona[] personas = new Persona[1500];

        
        String[] nombres = {
            "Juan", "Maria", "Carlos", "Ana", "Pedro",
            "Laura", "Andres", "Sofia", "Daniel", "Luis"
        };

        
        for (int i = 0; i < 1500; i++) {

            personas[i] = new Persona("1000" + i);

            personas[i].nombre = nombres[i % 10];
        }

        for (int i = 0; i < 1500; i++) {

            System.out.println("Persona: " + (i + 1));
            System.out.println("Nombre: " + personas[i].nombre);
            System.out.println("Cedula: " + personas[i].cedula);
            System.out.println("-------------------");
        }
    }
}
 
