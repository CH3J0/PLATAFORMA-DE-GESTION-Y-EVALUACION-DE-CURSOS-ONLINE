# PLATAFORMA
class Plataforma:
    def __init__(self):
        self.usuarios = {}
        self.cursos = {}
        
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            raise ValueError("ID de usuario ya existe.")
        self.usuarios[usuario.id_usuario] = usuario
        print(f"Usuario {usuario.nombre} registrado con éxito.")

    def crear_curso(self, codigo, nombre, id_instructor):
        if id_instructor not in self.usuarios or not isinstance(self.usuarios[id_instructor], Instructor):
            raise ValueError("Instructor no válido o no encontrado.")
        
        instructor = self.usuarios[id_instructor]
        nuevo_curso = Curso(codigo, nombre, instructor)
        self.cursos[codigo] = nuevo_curso
        instructor.agregar_curso(nuevo_curso)

    def inscribir_estudiante_en_curso(self, id_estudiante, codigo_curso):
        estudiante = self.usuarios.get(id_estudiante)
        curso = self.cursos.get(codigo_curso)
        
        if not isinstance(estudiante, Estudiante):
            print("ID de usuario no corresponde a un estudiante.")
            return
        if not curso:
            print("Código de curso no encontrado.")
            return
        
        curso.inscribir_estudiante(estudiante)

    def obtener_info_curso(self, codigo_curso):
        return self.cursos.get(codigo_curso)
