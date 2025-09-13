# USUARIO (hereda a estudiante e instructor)
class Usuario:
    def __init__(self, id_usuario, nombre, email):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        
    def __str__(self):
        return (
            f"--- BIENVENIDO USUARIO ---\n"
            f" - Nombre de usuario: {self.nombre}\n"
            f" - Id de usuario: {self.id_usuario}\n"
            f" - Correo electrónico de usuario: {self.email}"
        )

# Clase Estudiante
class Estudiante(Usuario):
    def __init__(self, id_usuario, nombre, email):
        super().__init__(id_usuario, nombre, email)
        self.cursos_inscritos = []
        self.calificaciones = {}

    def inscribir_curso(self, curso):
        if curso in self.cursos_inscritos:
            raise ValueError(f"El estudiante {self.nombre}, ya está inscrito en este curso")
        self.cursos_inscritos.append(curso)
        print(f"Estudiante: {self.nombre}, ha sido inscrito en el curso: {curso.nombre}")

    def asignar_calificacion(self, curso, nota):
        if curso not in self.cursos_inscritos:
            raise ValueError(f"No se puede asignar nota, el estudiante no está inscrito en: {curso.nombre}")
        self.calificaciones[curso.nombre] = nota
        print(f"Nota asignada en {curso.nombre}: {nota}")

    def obtener_cursos_inscritos(self):
        return [curso.nombre for curso in self.cursos_inscritos]

    def __str__(self):
        cursos = ', '.join(self.obtener_cursos_inscritos()) if self.cursos_inscritos else "Ninguno"
        calificaciones = (
            '\n'.join([f" °-° {curso}: {nota}" for curso, nota in self.calificaciones.items()])
            if self.calificaciones else "   - Sin calificaciones registradas"
        )
        return (
            super().__str__() + "\n"
            f" - Cursos inscritos: {cursos}\n"
            f" - Calificaciones:\n{calificaciones}"
        )
# Clase Instructor
class Instructor(Usuario):
    def __init__(self, id_usuario, nombre, email):
        super().__init__(id_usuario, nombre, email)
        self.cursos_impartidos = []

    def agregar_curso(self, curso):
        self.cursos_impartidos.append(curso)
        print(f"Curso {curso.nombre} agregado al instructor {self.nombre}")

    def obtener_cursos_impartidos(self):
        return [curso.nombre for curso in self.cursos_impartidos]

    def __str__(self):
        cursos = ', '.join(self.obtener_cursos_impartidos()) if self.cursos_impartidos else "Ninguno"
        return (
            super().__str__() + "\n"
            f" - Cursos impartidos: {cursos}"
        )
