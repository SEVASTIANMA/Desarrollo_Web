# ==========================================
# Implementación en Python a partir de Diagrama de Clases UML
# ==========================================

class Entrega:
    def __init__(self, fecha, tema, archivo_ruta):
        self.fecha = fecha
        self.tema = tema
        self.archivo_ruta = archivo_ruta
        self.estado = "Pendiente"

    def validar_archivo(self):
        return bool(self.archivo_ruta.strip())

    def marcar_revisada(self):
        if self.validar_archivo():
            self.estado = "Revisada"
        return self.estado

class Aprendiz:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha
        self.entregas = []

    def registrar_entrega(self, entrega):
        if entrega.validar_archivo():
            self.entregas.append(entrega)
            return True
        return False

aprendiz = Aprendiz("Jarid Osorio", "3532730")
entrega = Entrega("2026-11-18", "Diagrama de Clases UML", "2026-11-18_Python_Clase_Desde_UML.py")
entrega.marcar_revisada()
aprendiz.registrar_entrega(entrega)

print(f"Aprendiz: {aprendiz.nombre} | Entregas registradas: {len(aprendiz.entregas)} | Estado: {entrega.estado}")