class Main {
    public static void main(String[] args) {
         Computador com = new Computador("900 gb", "RTX 3060", "AMD Ryzen 7 7000", 32);
        com.teclado = "Teclado logitech a bluetooth";
        com.mouse = "Mouse logitech USB";
        com.so = "Windows 11";
        com.navegador = "Brave";
        System.out.println("Computador gamer " + com.so + " procesador " + com.cpu + " con GPU " + com.gpu + ", " + com.ram + " gb de RAM " + com.almacenamiento + "de almacenamiento.");
        System.out.println("Incluye: " + com.teclado + ", " + com.mouse + ", con navegador predeterminado " + com.navegador + ".");
    }
}

class Computador {
    public String almacenamiento;
    public String gpu;
    public String cpu;
    public int ram;
    public String teclado;
    public String mouse;
    public String so;
    public String navegador;

    Computador(String a, String g, String c, int ram){
        this.almacenamiento = a;
        this.gpu = g;
        this.cpu = c;
        this.ram = ram;
    }
}