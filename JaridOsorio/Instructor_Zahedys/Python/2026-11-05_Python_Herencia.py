# ==========================================
# Herencia y Polimorfismo en Python
# ==========================================

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar_info(self):
        return f"Usuario: {self.nombre}, Email: {self.email}"

class Aprendiz(Usuario):
    def __init__(self, nombre, email, ficha):
        super().__init__(nombre, email)
        self.ficha = ficha

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Ficha: {self.ficha}"

# Instancia de prueba
ap = Aprendiz("Jarid Osorio", "jarid@sena.edu.co", "3532730")
print("--- DATOS DEL APRENDIZ ---")
print(ap.mostrar_info())
