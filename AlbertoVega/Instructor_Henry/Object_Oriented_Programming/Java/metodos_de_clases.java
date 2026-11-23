class Main {
    public static void main(String[] args) {
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