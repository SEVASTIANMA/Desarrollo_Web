# ==========================================
# Representación legible de objetos con __str__
# ==========================================

class TareaADSO:
    def __init__(self, fecha, tema, herramienta, completada=False):
        self.fecha = fecha
        self.tema = tema
        self.herramienta = herramienta
        self.completada = completada

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"[{self.fecha}] {self.herramienta} - {self.tema} ({estado})"

tarea_hoy = TareaADSO("2026-11-13", "Modelado de clases", "Python")
tarea_hoy.marcar_completada()
print(tarea_hoy)
