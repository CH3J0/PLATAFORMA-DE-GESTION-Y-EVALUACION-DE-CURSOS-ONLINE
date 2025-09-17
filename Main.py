# USUARIO (hereda a estudiante e instructor) Clase base para todos los usuarios de la plataforma
class Usuario:
    def __init__(self, Carné_usuario, nombre, email):
        self.Carné_usuario = Carné_usuario
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return (
            f"--- BIENVENIDO USUARIO ---\n"
            f" - Nombre de usuario: {self.nombre}\n"
            f" - Carné de usuario: {self.Carné_usuario}\n"
            f" - Correo electrónico de usuario: {self.email}"
        )


# Clase Estudiante, Clase que representa a un estudiante
class Estudiante(Usuario):
    def __init__(self, Carné_usuario, nombre, email):
        super().__init__(Carné_usuario, nombre, email)
        self.cursos_inscritos = []
        self.calificaciones = {}

    def inscribir_curso(self, curso):
        if curso in self.cursos_inscritos:
            raise ValueError(f"El estudiante {self.nombre} ya está inscrito en este curso")
        self.cursos_inscritos.append(curso)
        print(f"Estudiante {self.nombre} ha sCarnéo inscrito en el curso: {curso.nombre}")

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
# Clase Instructor hereda de Usuario
class Instructor(Usuario):
    def __init__(self, Carné_usuario, nombre, email):
        super().__init__(Carné_usuario, nombre, email)
        self.cursos_impartCarnéos = []

    def agregar_curso(self, curso):
        self.cursos_impartCarnéos.append(curso)
        print(f"Curso {curso.nombre} agregado al instructor {self.nombre}")

    def obtener_cursos_impartCarnéos(self):
        return [curso.nombre for curso in self.cursos_impartCarnéos]

    def __str__(self):
        cursos = ', '.join(self.obtener_cursos_impartCarnéos()) if self.cursos_impartCarnéos else "Ninguno"
        return (
            super().__str__() + "\n"
            f" - Cursos impartCarnéos: {cursos}"
        )





# CUURSO (hereda a evalucacion)
class Curso:
    def __init__(self, codigo, nombre, instructor, **kwargs):
        self.codigo = codigo
        self.nombre = nombre
        self.instructor = instructor
        self.estudiantes_inscritos = []
        self.evaluaciones = []
        self.extra = kwargs  # Información adicional opcional

    def inscribir_estudiante(self, *estudiantes):
        for estudiante in estudiantes:
            if estudiante in self.estudiantes_inscritos:
                print(f"El estudiante {estudiante.nombre} ya está inscrito en el curso {self.nombre}.")
            else:
                try:
                    estudiante.inscribir_curso(self)
                    self.estudiantes_inscritos.append(estudiante)
                    print(f"Estudiante {estudiante.nombre} inscrito en el curso: {self.nombre}")
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
                print(f"    - {est.nombre} (Carné: {est.Carné_usuario})")
        else:
            print("    - Ninguno")
        print(f" - Evaluaciones creadas:")
        if self.evaluaciones:
            for ev in self.evaluaciones:
                print(f"    - {str(ev)}")
        else:
            print("    - Ninguna")
        if self.extra:
            print(f" - Información adicional del curso:")   # Aca se podra colocar información extra del curso
            for clave, valor in self.extra.items():         # Como activCarnéades extra, creditos del curso, horas
                print(f"    • {clave}: {valor}")            # Tipo de curso, etc.


# Clase base Evaluación
class Evaluacion:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
        self.notas = {}
  # {estudiante: nota}

    def asignar_nota(self, estudiante, nota):
        if estudiante not in self.curso.estudiantes_inscritos:
            raise ValueError(f"El estudiante {estudiante.nombre} no está inscrito en {self.curso.nombre}")
        self.notas[estudiante] = nota
        estudiante.asignar_calificacion(self.curso, nota)




# PLATAFORMA
class Plataforma:
    def __init__(self):
        self.usuarios = {}
        self.cursos = {}
        
    def registrar_usuario(self, usuario):
        if usuario.Carné_usuario in self.usuarios:
            raise ValueError("Carné de usuario ya existe.")
        self.usuarios[usuario.Carné_usuario] = usuario
        print(f"Usuario {usuario.nombre} registrado con éxito.")

    def crear_curso(self, codigo, nombre, Carné_instructor, **kwargs):
        if Carné_instructor not in self.usuarios or not isinstance(self.usuarios[Carné_instructor], Instructor):
            raise ValueError("Instructor no válido o no encontrado.")
        instructor = self.usuarios[Carné_instructor]
        nuevo_curso = Curso(codigo, nombre, instructor, **kwargs)
        self.cursos[codigo] = nuevo_curso
        instructor.agregar_curso(nuevo_curso)
        print(f"Curso {nombre} creado con parámetros extra: {kwargs}")   # Uso de kwargs

    def inscribir_estudiante_en_curso(self, codigo_curso, *Carnés_estudiantes):
        curso = self.cursos.get(codigo_curso)
        if not curso:
            print("Código de curso no encontrado.")
            return
        estudiantes = []
        for Carné_estudiante in Carnés_estudiantes:
            estudiante = self.usuarios.get(Carné_estudiante)
            if not isinstance(estudiante, Estudiante):
                print(f"Carné {Carné_estudiante} no corresponde a un estudiante o no existe.")
                continue
            estudiantes.append(estudiante)
        if estudiantes:
            curso.inscribir_estudiante(*estudiantes)

    def obtener_info_curso(self, codigo_curso):
        return self.cursos.get(codigo_curso)
    

# Tipos de activCarnéades (evaluaciones, tareas, etc)
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



# VALIDACIONES
def pedir_Carné():
    while True:
        Carné_usuario = input("Ingrese el Carné (solo números): ")
        if Carné_usuario.isdigit():
            return int(Carné_usuario)
        print("Error: El Carné debe contener solo números.")

def pedir_nombre():
    while True:
        nombre = input("Ingrese el nombre (sin números): ")
        if nombre.replace(" ", "").isalpha():
            return nombre
        print("Error: El nombre no debe contener números ni símbolos.")

def pedir_email():
    while True:
        email = input("Ingrese el correo electrónico: ")
        if "@" in email and "." in email:
            return email
        print("Error: El correo debe contener '@' y '.'")

def pedir_codigo():
    while True:
        codigo = input("Ingrese el código del curso (solo números): ")
        if codigo.isdigit():
            return int(codigo)
        print("Error: El código debe contener solo números.")

def pedir_nombre_curso():
    while True:
        nombre = input("Ingrese el nombre del curso (sin números): ")
        if nombre.replace(" ", "").isalpha():
            return nombre
        print("Error: El nombre no debe contener números ni símbolos.")

def pedir_nombre_evaluacion():
    while True:
        nombre = input("Ingrese el nombre de la evaluación: ")
        if nombre.strip():
            return nombre
        print("Error: El nombre no puede estar vacío.")

def pedir_tipo_evaluacion():
    while True:
        tipo = input("Ingrese el tipo de evaluación (Ej: Examen, Proyecto, Tarea): ")
        if tipo.replace(" ", "").isalpha():
            return tipo
        print("Error: El tipo debe contener solo letras.")


# Funciones de notas
notas = []  # Historial global de notas

def validar_nota(nota):
    if not isinstance(nota, (int, float)):
        raise TypeError("La nota debe ser un número")
    if nota < 0 or nota > 100:
        raise ValueError("La nota debe estar entre 0 y 100")

def registrar_historial(estudiante, evaluacion, nota):
    notas.append({
        "estudiante": estudiante.nombre,
        "evaluacion": evaluacion.nombre,
        "curso": evaluacion.curso.nombre,
        "nota": nota
    })

def asignar_nota_a_estudiante(evaluacion, estudiante, nota):
    try:
        validar_nota(nota)
        evaluacion.asignar_nota(estudiante, nota)
        registrar_historial(estudiante, evaluacion, nota)
        print(f"Nota {nota} asignada a {estudiante.nombre} en {evaluacion.nombre} ({evaluacion.curso.nombre})")
    except (ValueError, TypeError) as e:
        print(f"Error al asignar la nota: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def tipo_de_evaluacion(evaluacion):
    if isinstance(evaluacion, Examen):
        return "Examen"
    elif isinstance(evaluacion, Tarea):
        return "Tarea"
    elif isinstance(evaluacion, Proyecto):
        return "Proyecto"
    else:
        return "Evaluacion"

def reporte_promedio_bajo(curso, umbral=60):  #Genera un reporte de estudiantes con promedio menor al umbral
    print(f"\n--- REPORTE: Estudiantes con promedio menor a {umbral} ---")  # Umbra: Valor mínimo de las notas
    for estudiante in curso.estudiantes_inscritos:
        notas_est = [
            (eval.nombre, tipo_de_evaluacion(eval), eval.notas[estudiante])
            for eval in curso.evaluaciones if estudiante in eval.notas
        ]
        if notas_est:
            promedio = sum(n[2] for n in notas_est) / len(notas_est)
            if promedio < umbral:
                print(f"\nEstudiante: {estudiante.nombre} | Carné: {estudiante.Carné_usuario} | Email: {estudiante.email}")
                print(f"Promedio: {promedio:.2f}")
                print("Notas por evaluación:")
                for nombre_eval, tipo, nota in notas_est:
                    print(f"  - {nombre_eval} ({tipo}): {nota}")
        else:
            print(f"\nEstudiante: {estudiante.nombre} | Carné: {estudiante.Carné_usuario} | Email: {estudiante.email}")
            print("  - No tiene notas registradas.")



# MENU
def menu_principal(plataforma):
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar nuevo usuario")
        print("2. Acceder como usuario existente")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("¿Es Estudiante (E) o Instructor (I)? ").strip().upper()
            Carné_usuario = pedir_Carné()
            if Carné_usuario in plataforma.usuarios:
                print("Ya existe un usuario con ese Carné. Use la opción 2 para acceder.")
                continue
            nombre = pedir_nombre()
            email = pedir_email()
            if tipo == "E":
                usuario = Estudiante(Carné_usuario, nombre, email)
            elif tipo == "I":
                usuario = Instructor(Carné_usuario, nombre, email)
            else:
                print("Tipo no válido.")
                continue

            plataforma.registrar_usuario(usuario)
            guardar_usuarios_txt(plataforma)

        elif opcion == "2":
            Carné_usuario = pedir_Carné()
            usuario = plataforma.usuarios.get(Carné_usuario)
            if usuario:
                if isinstance(usuario, Estudiante):
                    menu_estudiante(usuario)
                elif isinstance(usuario, Instructor):
                    menu_instructor(usuario, plataforma)
            else:
                print("Usuario no encontrado. Regístrese primero.")

        elif opcion == "3":   # nos sacara del sistema
            guardar_cursos_txt(plataforma)
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")


# Funcion Menu estudiante
def menu_estudiante(estudiante):
    while True:
        print(f"\n--- MENÚ ESTUDIANTE ({estudiante.nombre}) ---")
        print("1. Ver cursos inscritos")
        print("2. Ver calificaciones")
        print("3. Ver perfil")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cursos = estudiante.obtener_cursos_inscritos()
            print("Cursos inscritos:", ", ".join(cursos) if cursos else "Ninguno")

        elif opcion == "2":
            if estudiante.calificaciones:
                print("Calificaciones:")
                for curso, nota in estudiante.calificaciones.items():
                    print(f" - {curso}: {nota}")
            else:
                print("No hay calificaciones registradas.")

        elif opcion == "3":
            print(estudiante)

        elif opcion == "4":
            break

        else:
            print("Opción no válida.")
            

# Funcion menu instructor
def menu_instructor(instructor, plataforma):
    while True:
        print(f"\n--- MENÚ INSTRUCTOR ({instructor.nombre}) ---")
        print("1. Crear curso")
        print("2. Crear evaluación")
        print("3. Asignar calificación a estudiante")
        print("4. Inscribir estudiante en curso")
        print("5. Ver cursos impartCarnéos")
        print("6. Ver perfil")
        print("7. Ver historial de notas")
        print("8. Generar reporte de promedio bajo")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = pedir_codigo()
            nombre = pedir_nombre_curso()
            try:
                plataforma.crear_curso(codigo, nombre, instructor.Carné_usuario)
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            codigo = pedir_codigo()
            curso = plataforma.obtener_info_curso(codigo)
            if curso and curso.instructor == instructor:
                nombre_eval = pedir_nombre_evaluacion()
                tipo_eval = pedir_tipo_evaluacion()

                if tipo_eval.lower() == "examen":
                    duracion = int(input("Duración en minutos: "))
                    evaluacion = Examen(nombre_eval, curso, duracion)
                elif tipo_eval.lower() == "tarea":
                    fecha_entrega = input("Fecha de entrega: ")
                    evaluacion = Tarea(nombre_eval, curso, fecha_entrega)
                elif tipo_eval.lower() == "proyecto":
                    porcentaje = float(input("Porcentaje del proyecto: "))
                    evaluacion = Proyecto(nombre_eval, curso, porcentaje)
                else:
                    evaluacion = Evaluacion(nombre_eval, curso)

                curso.crear_evaluacion(evaluacion)
            else:
                print("Curso no encontrado o no pertenece al instructor.")

        elif opcion == "3":
            codigo = pedir_codigo()
            curso = plataforma.obtener_info_curso(codigo)
            if curso and curso.instructor == instructor and curso.evaluaciones:
                print("Evaluaciones disponibles:")
                for i, ev in enumerate(curso.evaluaciones):
                    print(f"{i + 1}. {ev.nombre} ({tipo_de_evaluacion(ev)})")
                try:
                    indice = int(input("Seleccione evaluación: ")) - 1
                    evaluacion = curso.evaluaciones[indice]
                except (ValueError, IndexError):
                    print("Selección inválida.")
                    continue

                Carné_estudiante = pedir_Carné()
                estudiante = plataforma.usuarios.get(Carné_estudiante)
                if isinstance(estudiante, Estudiante):
                    nota = input("Ingrese la nota: ")
                    try:
                        asignar_nota_a_estudiante(evaluacion, estudiante, float(nota))
                    except Exception as e:
                        print(f"Error: {e}")
                else:
                    print("Carné inválido o no corresponde a un estudiante.")
            else:
                print("Curso no válido o sin evaluaciones.")

        elif opcion == "4":
            Carné_estudiante = pedir_Carné()
            codigo = pedir_codigo()
            estudiante = plataforma.usuarios.get(Carné_estudiante)
            curso = plataforma.cursos.get(codigo)
            if isinstance(estudiante, Estudiante) and curso and curso.instructor == instructor:
                curso.inscribir_estudiante(estudiante)
            else:
                print("Datos inválidos o curso no pertenece al instructor.")

        elif opcion == "5":
            cursos = instructor.obtener_cursos_impartCarnéos()
            print("Cursos impartCarnéos:", ", ".join(cursos) if cursos else "Ninguno")

        elif opcion == "6":
            print(instructor)

        elif opcion == "7":
            print("\n--- HISTORIAL DE NOTAS ---")
            for registro in notas:
                print(f"{registro['estudiante']} - {registro['curso']} - {registro['evaluacion']}: {registro['nota']}")

        elif opcion == "8":
            codigo = pedir_codigo()
            curso = plataforma.obtener_info_curso(codigo)
            if curso and curso.instructor == instructor:
                reporte_promedio_bajo(curso)
            else:
                print("Curso no encontrado o no pertenece al instructor.")

        elif opcion == "9":
            break

        else:
            print("Opción no válida.")


#Funciones para guardar informacion en un txt
def guardar_usuarios_txt(plataforma, archivo="usuarios.txt"):
    with open(archivo, "w", encoding="utf-8") as f:
        for usuario in plataforma.usuarios.values():
            tipo = "Estudiante" if isinstance(usuario, Estudiante) else "Instructor"
            f.write(f"{usuario.Carné_usuario},{usuario.nombre},{usuario.email},{tipo}\n")

def cargar_usuarios_txt(plataforma, archivo="usuarios.txt"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                Carné_usuario, nombre, email, tipo = linea.strip().split(",")
                Carné_usuario = int(Carné_usuario)
                if tipo == "Estudiante":
                    usuario = Estudiante(Carné_usuario, nombre, email)
                else:
                    usuario = Instructor(Carné_usuario, nombre, email)
                plataforma.registrar_usuario(usuario)
    except FileNotFoundError:
        print("Archivo de usuarios no encontrado. Se iniciará vacío.")


# Funcion para guardar la informacion de los cursos en un txt
def guardar_cursos_txt(plataforma, archivo="cursos.txt"):
    with open(archivo, "w", encoding="utf-8") as f:
        for curso in plataforma.cursos.values():
            f.write(f"--- CURSO ---\n")
            f.write(f"Código: {curso.codigo}\n")
            f.write(f"Nombre: {curso.nombre}\n")
            f.write(f"Instructor: {curso.instructor.nombre} (Carné: {curso.instructor.Carné_usuario})\n")

            f.write("Estudiantes inscritos:\n")
            if curso.estudiantes_inscritos:
                for est in curso.estudiantes_inscritos:
                    f.write(f" - {est.nombre} (Carné: {est.Carné_usuario})\n")
            else:
                f.write(" - Ninguno\n")

            f.write("Evaluaciones:\n")
            if curso.evaluaciones:
                for ev in curso.evaluaciones:
                    f.write(f" - {ev.nombre} ({tipo_de_evaluacion(ev)})\n")
            else:
                f.write(" - Ninguna\n")

            if curso.extra:
                f.write("Información adicional:\n")
                for clave, valor in curso.extra.items():
                    f.write(f" • {clave}: {valor}\n")

            f.write("\n")  # ESto solo separara la informacion de cada curso


# INSTANCIA GENERAL
plataforma = Plataforma()
cargar_usuarios_txt(plataforma)
menu_principal(plataforma)
