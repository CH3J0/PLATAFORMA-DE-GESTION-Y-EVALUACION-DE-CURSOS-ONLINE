# clase usuario, para conocer la información del usuario
class Usuario:
    def __init__(self, id_usuario, nombre, email):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        
    def __str__(self):
        return (
            f"--- BIENVENIDO USUARIO ---\n"             # Presentamos al usuario 
            f" - Nombre de usuario: {self.nombre}\n"
            f" - Id de usuario: {self.id_usuario}\n"
            f" - Correo electrónico de usuario: {self.email}"
        )


# Clase Estudiante, esta heredará de usuario
class Estudiante(Usuario):
    def __init__(self, id_usuario, nombre, email):
        super().__init__(id_usuario, nombre, email)
        self.cursos_inscritos = []  # Lista para los cursos inscritos
        self.calificaciones = {}    # Voy a usar un diccionario para que se guarden las calificaciones

    def inscribir_curso(self, curso):  # Verificamos si el estudiante ya está inscrito
        if curso in self.cursos_inscritos:
            raise ValueError(f"El estudiante {self.nombre}, ya está inscrito en este curso")
        self.cursos_inscritos.append(curso)
        print(f"Estudiante: {self.nombre}, ha sido inscrito en el curso: {curso.nombre}")

    def asignar_calificacion(self, curso, nota):  # Asignamos una nota al curso si está inscrito
        if curso not in self.cursos_inscritos:
            raise ValueError(f"No se puede asignar nota, el estudiante no está inscrito en: {curso.nombre}")
        self.calificaciones[curso.nombre] = nota
        print(f"Nota asignada en {curso.nombre}: {nota}")

    def obtener_cursos_inscritos(self):  # Retorna los nombres de los cursos inscritos
        return [curso.nombre for curso in self.cursos_inscritos]

    def __str__(self):  # Mostramos información extendida del estudiante
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


# Clase Instructor, también heredará de usuario
class Instructor(Usuario):
    def __init__(self, id_usuario, nombre, email):
        super().__init__(id_usuario, nombre, email)
        self.cursos_impartidos = []  # Una lista para los cursos que imparte

    def agregar_curso(self, curso):  # Agregamos un curso que el instructor impartirá
        self.cursos_impartidos.append(curso)
        print(f"Curso {curso.nombre} agregado al instructor {self.nombre}")

    def obtener_cursos_impartidos(self):  # Retorna los nombres de los cursos impartidos
        return [curso.nombre for curso in self.cursos_impartidos]

    def __str__(self):  # Mostramos información extendida del instructor
        cursos = ', '.join(self.obtener_cursos_impartidos()) if self.cursos_impartidos else "Ninguno"
        return (
            super().__str__() + "\n"
            f" - Cursos impartidos: {cursos}"
        )
