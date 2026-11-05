# ==========================================
# Programación Orientada a Objetos en Python
# ==========================================

class SoftwareProject:
    def __init__(self, nombre, lenguaje, horas_estimadas):
        self.nombre = nombre
        self.lenguaje = lenguaje
        self.horas_estimadas = horas_estimadas
        self.completado = False

    def registrar_avance(self, horas_trabajadas):
        self.horas_estimadas -= horas_trabajadas
        if self.horas_estimadas <= 0:
            self.completado = True
            print(f"🎉 El proyecto '{self.nombre}' ha sido finalizado.")
        else:
            print(f"⏱️ Horas restantes para '{self.nombre}': {self.horas_estimadas} hrs.")

# Instancia de prueba
mi_proyecto = SoftwareProject("App Móvil ADSO", "Dart", 20)
mi_proyecto.registrar_avance(12)
mi_proyecto.registrar_avance(8)