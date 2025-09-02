# Clase Curso para gestionar la información de los cursos
class Curso:
    def __init__(self, codigo, nombre, instructor):
        self.codigo = codigo
        self.nombre = nombre
        self.instructor = instructor
        self.estudiantes_inscritos = [] #Una lista para los objetos
        self.evaluaciones = []       
