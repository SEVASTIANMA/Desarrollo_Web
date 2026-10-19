class Estudiante:
    def __init__(self, persona):
        self.persona = persona

estudiantes = []

for i in range(1, 1501):
    estudiantes.append(Estudiante(f"Persona{i}"))

for estudiante in estudiantes:
    print(estudiante.persona)