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

# Clase Estudiante, esta heredara de usuario
class Estudiante(Usuario):
    def __init__(self, id_usuario, nombre, email):
        super().__init__(id_usuario, nombre, email)
        self.cursos_inscritos = []  # Lista para lso cursos inscritos
        self.calificaciones = {}   #voy a usar un diccionario para q se guarden las calificaciones

    def inscribir_curso(self, curso):               #Un error, para ver si el estudiante ya esta inscrito
        if curso in self.cursos_inscritos:
            raise ValueError(f"El estudiante {self.nombre}, ya está inscrito en este curso")
        self.cursos_inscritos.append(curso)
        print(f"Estudiante: {self.nombre}, ha sido inscrito en el curso: {curso.nombre}")

    def obtener_cursos_inscritos(self):
        return self.cursos_inscritos

# Clase Instructo, tambien heredara a usuario
class Instructor(Usuario):
    def __init__(self, id_usuario, nombre, email):
        super().__init__(id_usuario, nombre, email)
        self.cursos_impartidos = []  #Una lista para los cursos q imparte
