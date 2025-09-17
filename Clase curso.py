# CUURSO (hereda a evalucacion)
class Curso:
    def __init__(self, codigo, nombre, instructor):
        self.codigo = codigo
        self.nombre = nombre
        self.instructor = instructor
        self.estudiantes_inscritos = []
        self.evaluaciones = []

    def inscribir_estudiante(self, estudiante):
        if estudiante in self.estudiantes_inscritos:
            print(f"El estudiante {estudiante.nombre} ya está inscrito en el curso {self.nombre}.")
            return
        try:
            estudiante.inscribir_curso(self)
            self.estudiantes_inscritos.append(estudiante)
        except ValueError as e:
            print(f"Error al inscribir estudiante: {e}")

    def crear_evaluacion(self, evaluacion):
        if any(ev.nombre == evaluacion.nombre for ev in self.evaluaciones):
            print(f"Ya existe una evaluación llamada '{evaluacion.nombre}' en este curso.")
            return
        self.evaluaciones.append(evaluacion)
        print(f"Evaluación {evaluacion.nombre} creada para el curso: {self.nombre}")

    def mostrar_info_completa(self):
        print(f"\n--- INFORMACIÓN DEL CURSO ---")
        print(f" - Código: {self.codigo}")
        print(f" - Nombre: {self.nombre}")
        print(f" - Instructor: {self.instructor.nombre}")
        print(f" - Estudiantes inscritos:")
        if self.estudiantes_inscritos:
            for est in self.estudiantes_inscritos:
                print(f"    - {est.nombre} (ID: {est.id_usuario})")
        else:
            print("    - Ninguno")
        print(f" - Evaluaciones creadas:")
        if self.evaluaciones:
            for ev in self.evaluaciones:
                print(f"    - {str(ev)}")
        else:
            print("    - Ninguna")

class Evaluacion:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo  

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"
