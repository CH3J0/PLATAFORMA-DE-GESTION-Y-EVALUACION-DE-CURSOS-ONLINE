# CLASE BASE DE EVALUACIÓN

class Evaluacion:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
        self.notas = {}  # {estudiante: nota}

    def asignar_nota(self, estudiante, nota):
        if estudiante not in self.curso.estudiantes_inscritos:
            raise ValueError(f"El estudiante {estudiante.nombre} no está inscrito en {self.curso.nombre}")
        self.notas[estudiante] = nota
        estudiante.asignar_calificacion(self.curso, nota)

    def __str__(self):
        return f"Evaluación: {self.nombre}"

class Examen(Evaluacion):
    def __init__(self, nombre, curso, duracion):
        super().__init__(nombre, curso)
        self.duracion = duracion

    def __str__(self):
        return f"Examen: {self.nombre}, Duración: {self.duracion} min"
    
class Tarea(Evaluacion):
    def __init__(self, nombre, curso, fecha_entrega):
        super().__init__(nombre, curso)
        self.fecha_entrega = fecha_entrega

    def __str__(self):
        return f"Tarea: {self.nombre}, Entrega: {self.fecha_entrega}"

class Proyecto(Evaluacion):
    def __init__(self, nombre, curso, porcentaje):
        super().__init__(nombre, curso)
        self.porcentaje = porcentaje

    def __str__(self):
        return f"Proyecto: {self.nombre}, Valor: {self.porcentaje}%"