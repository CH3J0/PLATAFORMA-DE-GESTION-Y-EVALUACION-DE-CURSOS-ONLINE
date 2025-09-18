# ============================
# CLASE BASE: USUARIO
# ============================

class Usuario:
    def __init__(self, Carné_usuario, nombre, email):
        # Constructor de la clase base Usuario.
        # Aquí se inicializan los atributos comunes para cualquier tipo de usuario.
        self.Carné_usuario = Carné_usuario  # Identificador único del usuario
        self.nombre = nombre                # Nombre del usuario
        self.email = email                  # Correo electrónico del usuario

    def __str__(self):
        # Método especial que define cómo se representa un objeto Usuario como cadena.
        return (
            f"--- BIENVENIDO USUARIO ---\n"
            f" - Nombre de usuario: {self.nombre}\n"
            f" - Carné de usuario: {self.Carné_usuario}\n"
            f" - Correo electrónico de usuario: {self.email}"
        )

# ============================
# CLASE HEREDADA DE USUARIO: ESTUDIANTE
# ============================

class Estudiante(Usuario):
    def __init__(self, Carné_usuario, nombre, email):
        # Constructor de la clase Estudiante.
        # Llama al constructor de Usuario con super() para reutilizar atributos comunes.
        super().__init__(Carné_usuario, nombre, email)

        # Atributos específicos del estudiante:
        self.cursos_inscritos = []     # Lista que almacenará objetos de tipo Curso
        self.calificaciones = {}       # Diccionario que mapea nombre del curso a nota

    def inscribir_curso(self, curso):
        # Método para inscribir al estudiante en un curso.
        # Se valida que el curso no esté ya inscrito para evitar duplicados.
        if curso in self.cursos_inscritos:
            raise ValueError(f"El estudiante {self.nombre} ya está inscrito en este curso")
        
        # Si pasa la validación, se agrega el curso a la lista.
        self.cursos_inscritos.append(curso)
        print(f"Estudiante {self.nombre} se ha inscrito en el curso: {curso.nombre}")

    def asignar_calificacion(self, curso, nota):
        # Método para asignar una calificación a un curso específico.
        # Solo se permite si el estudiante está inscrito en ese curso.
        if curso not in self.cursos_inscritos:
            raise ValueError(f"No se puede asignar nota, el estudiante no está inscrito en: {curso.nombre}")
        
        # Se guarda la nota en el diccionario usando el nombre del curso como clave.
        self.calificaciones[curso.nombre] = nota
        print(f"Nota asignada en {curso.nombre}: {nota}")

    def obtener_cursos_inscritos(self):
        # Método que devuelve una lista de nombres de cursos inscritos.
        # Esto facilita la visualización sin exponer directamente los objetos d Curso.
        return [curso.nombre for curso in self.cursos_inscritos]

    def __str__(self):
        # Método especial que extiende la representación del usuario.      
        # Si hay cursos inscritos, se listan por nombre; si no, se indica "Ninguno".
        cursos = ', '.join(self.obtener_cursos_inscritos()) if self.cursos_inscritos else "Ninguno"
        
        # Si hay calificaciones registradas, se formatea cada una; si no, se indica que no hay.
        calificaciones = (
            '\n'.join([f" °-° {curso}: {nota}" for curso, nota in self.calificaciones.items()])
            if self.calificaciones else "   - Sin calificaciones registradas"
        )

        # Se concatena la representación base del Usuario con los datos específicos del Estudiante.
        return (
            super().__str__() + "\n"
            f" - Cursos inscritos: {cursos}\n"
            f" - Calificaciones:\n{calificaciones}"
        )

# ============================
# CLASE INSTRUCTOR
# ============================

class Instructor(Usuario):
    def __init__(self, Carné_usuario, nombre, email):
        # Constructor que inicializa un instructor como un tipo de Usuario
        # Se reutilizan los atributos comunes con herencia
        super().__init__(Carné_usuario, nombre, email)

        # Atributo específico del instructor: lista de cursos que imparte
        self.cursos_impartidos = []  # contiene objetos de tipo Curso

    def agregar_curso(self, curso):
        # Método para asociar un curso al instructor
        self.cursos_impartidos.append(curso)
        print(f"Curso {curso.nombre} agregado al instructor {self.nombre}")

    def obtener_cursos_impartidos(self):
        # Devuelve una lista con los nombres de los cursos que imparte el instructor
        return [curso.nombre for curso in self.cursos_impartidos]

    def __str__(self):
        # Representación legible del instructor, incluyendo sus cursos
        cursos = ', '.join(self.obtener_cursos_impartidos()) if self.cursos_impartidos else "Ninguno"
        return (
            super().__str__() + "\n"
            f" - Cursos impartidos: {cursos}"
        )

# ============================
# CLASE CURSO
# ============================

class Curso:
    def __init__(self, codigo, nombre, instructor, **kwargs):
        # Constructor que define los atributos esenciales del curso
        self.codigo = codigo                  # Código único del curso
        self.nombre = nombre                  # Nombre del curso
        self.instructor = instructor          # Objeto Instructor que lo imparte
        self.estudiantes_inscritos = []       # Lista de objetos Estudiante inscritos
        self.evaluaciones = []                # Lista de objetos Evaluacion creados
        self.extra = kwargs                   # Diccionario para metadatos opcionales (ej. horario, modalidad)

    def inscribir_estudiante(self, *estudiantes):
        # Método para inscribir uno o más estudiantes en el curso
        for estudiante in estudiantes:
            if estudiante in self.estudiantes_inscritos:
                print(f"El estudiante {estudiante.nombre} ya está inscrito en el curso {self.nombre}.")
            else:
                try:
                    # Se actualiza también el estado del estudiante
                    estudiante.inscribir_curso(self)
                    self.estudiantes_inscritos.append(estudiante)
                    print(f"Estudiante {estudiante.nombre} inscrito en el curso: {self.nombre}")
                except ValueError as e:
                    # Captura errores de inscripción desde el lado del estudiante
                    print(f"Error al inscribir estudiante: {e}")

    def crear_evaluacion(self, evaluacion):
        # Método para agregar una evaluación al curso
        # Previene duplicados por nombre de evaluación
        if any(ev.nombre == evaluacion.nombre for ev in self.evaluaciones):
            print(f"Ya existe una evaluación llamada '{evaluacion.nombre}' en este curso.")
            return
        self.evaluaciones.append(evaluacion)
        print(f"Evaluación {evaluacion.nombre} creada para el curso: {self.nombre}")

    def mostrar_info_completa(self):
        # Método para imprimir todos los detalles del curso
        print(f"\n--- INFORMACIÓN DEL CURSO ---")
        print(f" - Código: {self.codigo}")
        print(f" - Nombre: {self.nombre}")
        print(f" - Instructor: {self.instructor.nombre}")

        # Listado de estudiantes inscritos
        print(f" - Estudiantes inscritos:")
        if self.estudiantes_inscritos:
            for est in self.estudiantes_inscritos:
                print(f"    - {est.nombre} (Carné: {est.Carné_usuario})")
        else:
            print("    - Ninguno")

        # Listado de evaluaciones creadas
        print(f" - Evaluaciones creadas:")
        if self.evaluaciones:
            for ev in self.evaluaciones:
                print(f"    - {str(ev)}")
        else:
            print("    - Ninguna")

        # Información adicional opcional
        if self.extra:
            print(f" - Información adicional del curso:")
            for clave, valor in self.extra.items():
                print(f"    • {clave}: {valor}")

# ============================
# CLASE BASE: EVALUACION
# ============================

class Evaluacion:
    def __init__(self, nombre, curso):
        # Constructor que define una evaluación asociada a un curso
        self.nombre = nombre              # Nombre de la evaluación 
        self.curso = curso                # Curso al que pertenece
        self.notas = {}                   # Diccionario con estudiantes como clave y nota como valor

    def asignar_nota(self, estudiante, nota):
        # Método para asignar una nota a un estudiante
        # Verifica que el estudiante esté inscrito en el curso antes de asignar
        if estudiante not in self.curso.estudiantes_inscritos:
            raise ValueError(f"El estudiante {estudiante.nombre} no está inscrito en {self.curso.nombre}")
        
        # Se guarda la nota en la evaluación y se actualiza también en el estudiante
        self.notas[estudiante] = nota
        estudiante.asignar_calificacion(self.curso, nota)

    def __str__(self):
        # Representación legible de la evaluación (nombre y cantidad de notas asignadas)
        return f"{self.nombre} ({len(self.notas)} notas registradas)"


# ============================
# CLASE PLATAFORMA
# ============================

class Plataforma:
    def __init__(self):
        # Diccionario que almacena todos los usuarios registrados en la plataforma
        # La clave es el Carné único de cada usuario
        self.usuarios = {}

        # Diccionario que almacena todos los cursos creados en la plataforma
        # La clave es el código único de cada curso
        self.cursos = {}

    def registrar_usuario(self, usuario):
        # Método para registrar un nuevo usuario 
        # Se verifica que el Carné no esté duplicado 
        if usuario.Carné_usuario in self.usuarios:
            raise ValueError("Carné de usuario ya existe.")
        
        # Si el Carné es único, se agrega al diccionario de usuarios
        self.usuarios[usuario.Carné_usuario] = usuario
        print(f"Usuario {usuario.nombre} registrado con éxito.")

    def crear_curso(self, codigo, nombre, Carné_instructor, **kwargs):
        # Método para crear un nuevo curso y asociarlo a un instructor existente
        # Se valida que el Carné pertenezca a un usuario de tipo Instructor
        if Carné_instructor not in self.usuarios or not isinstance(self.usuarios[Carné_instructor], Instructor):
            raise ValueError("Instructor no válido o no encontrado.")
        
        # SI es asi, se crea el curso
        instructor = self.usuarios[Carné_instructor]
        nuevo_curso = Curso(codigo, nombre, instructor, **kwargs)

        # Se registra el curso en el diccionario de cursos
        self.cursos[codigo] = nuevo_curso

        # Se asocia el curso al instructor mediante su método 
        instructor.agregar_curso(nuevo_curso)
        print(f"Curso {nombre} creado con parámetros extra: {kwargs}")

    def inscribir_estudiante_en_curso(self, codigo_curso, *Carnés_estudiantes):
        # Método para inscribir uno o más estudiantes en un curso existente
        # Se busca el curso por su código
        curso = self.cursos.get(codigo_curso)
        if not curso:
            print("Código de curso no encontrado.")
            return

        # Lista temporal para almacenar estudiantes válidos
        estudiantes = []
        for Carné_estudiante in Carnés_estudiantes:
            # Se busca el usuario por Carné y se valida que sea un Estudiante
            estudiante = self.usuarios.get(Carné_estudiante)
            if not isinstance(estudiante, Estudiante):
                print(f"Carné {Carné_estudiante} no corresponde a un estudiante o no existe.")
                continue
            estudiantes.append(estudiante)

        # Si hay estudiantes válidos, se inscriben en el curso
        if estudiantes:
            curso.inscribir_estudiante(*estudiantes)

    def obtener_info_curso(self, codigo_curso):
        # Método para obtener el objeto Curso a partir de su código
        return self.cursos.get(codigo_curso)

# ============================
# SUBCLASES DE EVALUACION
# ============================

class Examen(Evaluacion):
    def __init__(self, nombre, curso, duracion):
        # Constructor que extiende la clase Evaluacion
        # se añade atributo especifico
        super().__init__(nombre, curso)
        self.duracion = duracion

    def __str__(self):
        # Representación legible del examen, incluyendo duración
        return f"Examen: {self.nombre}, Duración: {self.duracion} min"

class Tarea(Evaluacion):
    def __init__(self, nombre, curso, fecha_entrega):
        # Constructor que extiende Evaluacion
        # Se añade el atributo específico 
        super().__init__(nombre, curso)
        self.fecha_entrega = fecha_entrega

    def __str__(self):
        # Representación legible de la tarea, incluyendo fecha de entrega
        return f"Tarea: {self.nombre}, Entrega: {self.fecha_entrega}"

class Proyecto(Evaluacion):
    def __init__(self, nombre, curso, porcentaje):
        # Constructor que extiende Evaluacion
        # Se añade el atributo específico 
        super().__init__(nombre, curso)
        self.porcentaje = porcentaje

    def __str__(self):
        # Representación legible del proyecto, incluyendo su valor porcentual
        return f"Proyecto: {self.nombre}, Valor: {self.porcentaje}%"

# ============================
# VALIDACIONES DE ENTRADA
# ============================

def pedir_Carné():
    # Solicita al usuario un Carné compuesto solo por números
    while True:
        Carné_usuario = input("Ingrese el Carné (solo números): ")
        if Carné_usuario.isdigit():  # Verifica que todos los caracteres sean dígitos
            return int(Carné_usuario)
        print("Error: El Carné debe contener solo números.")

def pedir_nombre():
    # Solicita un nombre sin números ni símbolos
    while True:
        nombre = input("Ingrese el nombre (sin números): ")
        if nombre.replace(" ", "").isalpha():  # Permite espacios pero no números ni símbolos
            return nombre
        print("Error: El nombre no debe contener números ni símbolos.")

def pedir_email():
    # Solicita un correo electrónico con formato básico válido
    while True:
        email = input("Ingrese el correo electrónico: ")
        if "@" in email and "." in email:  # Verifica que tenga al menos '@' y '.'
            return email
        print("Error: El correo debe contener '@' y '.'")

def pedir_codigo():
    # Solicita el código del curso
    while True:
        codigo = input("Ingrese el código del curso (solo números): ")
        if codigo.isdigit():
            return int(codigo)
        print("Error: El código debe contener solo números.")

def pedir_nombre_curso():
    # Solicita el nombre del curso sin números ni símbolos
    while True:
        nombre = input("Ingrese el nombre del curso (sin números): ")
        if nombre.replace(" ", "").isalpha():
            return nombre
        print("Error: El nombre no debe contener números ni símbolos.")

def pedir_nombre_evaluacion():
    # Solicita el nombre de la evaluación, asegurando que no esté vacío
    while True:
        nombre = input("Ingrese el nombre de la evaluación: ")
        if nombre.strip():  # Verifica que no sea solo espacios
            return nombre
        print("Error: El nombre no puede estar vacío.")

def pedir_tipo_evaluacion():
    # Solicita el tipo de evaluación 
    while True:
        tipo = input("Ingrese el tipo de evaluación (Ej: Examen, Proyecto, Tarea): ")
        if tipo.replace(" ", "").isalpha():  # Permite espacios pero no números ni símbolos
            return tipo
        print("Error: El tipo debe contener solo letras.")


# Funciones de notas
notas = []  # Lista global que almacena el historial de notas asignadas

def validar_nota(nota):
    # Verifica que la nota sea un número válido entre 0 y 100
    if not isinstance(nota, (int, float)):
        raise TypeError("La nota debe ser un número")
    if nota < 0 or nota > 100:
        raise ValueError("La nota debe estar entre 0 y 100")

def registrar_historial(estudiante, evaluacion, nota):
    # Registra la nota en el historial global con detalles del estudiante, curso y evaluación
    notas.append({
        "estudiante": estudiante.nombre,
        "evaluacion": evaluacion.nombre,
        "curso": evaluacion.curso.nombre,
        "nota": nota
    })

def asignar_nota_a_estudiante(evaluacion, estudiante, nota):
    # Asigna una nota a un estudiante en una evaluación específica
    try:
        validar_nota(nota)  # Verifica que la nota sea válida
        evaluacion.asignar_nota(estudiante, nota)  # Asigna la nota en el objeto Evaluacion
        registrar_historial(estudiante, evaluacion, nota)  # Guarda en historial
        print(f"Nota {nota} asignada a {estudiante.nombre} en {evaluacion.nombre} ({evaluacion.curso.nombre})")
    except (ValueError, TypeError) as e:
        print(f"Error al asignar la nota: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def tipo_de_evaluacion(evaluacion):
    # Determina el tipo de evaluación según su clase
    if isinstance(evaluacion, Examen):
        return "Examen"
    elif isinstance(evaluacion, Tarea):
        return "Tarea"
    elif isinstance(evaluacion, Proyecto):
        return "Proyecto"
    else:
        return "Evaluacion"  # SI no es especifica, coloca evaluacion
    

def reporte_promedio_bajo(curso, umbral=60):
    # Genera un reporte de estudiantes con promedio menor al umbral especificado
    print(f"\n--- REPORTE: Estudiantes con promedio menor a {umbral} ---")

    for estudiante in curso.estudiantes_inscritos:
        # Extrae todas las notas del estudiante en el curso
        notas_est = [
            (eval.nombre, tipo_de_evaluacion(eval), eval.notas[estudiante])
            for eval in curso.evaluaciones if estudiante in eval.notas
        ]

        if notas_est:
            # Calcula el promedio de las notas
            promedio = sum(n[2] for n in notas_est) / len(notas_est)
            if promedio < umbral:
                # Muestra detalles del estudiante y sus notas si el promedio es bajo
                print(f"\nEstudiante: {estudiante.nombre} | Carné: {estudiante.Carné_usuario} | Email: {estudiante.email}")
                print(f"Promedio: {promedio:.2f}")
                print("Notas por evaluación:")
                for nombre_eval, tipo, nota in notas_est:
                    print(f"  - {nombre_eval} ({tipo}): {nota}")
        else:
            # Si no tiene notas registradas, también se informa
            print(f"\nEstudiante: {estudiante.nombre} | Carné: {estudiante.Carné_usuario} | Email: {estudiante.email}")
            print("  - No tiene notas registradas.")

# ============================
# MENÚ PRINCIPAL
# ============================

def menu_principal(plataforma):
    # Ciclo principal del sistema que permite registrar usuarios, acceder o salir
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar nuevo usuario")
        print("2. Acceder como usuario existente")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Registro de nuevo usuario (Estudiante o Instructor)
            tipo = input("¿Es Estudiante (E) o Instructor (I)? ").strip().upper()
            Carné_usuario = pedir_Carné()

            # Verifica si el Carné ya está registrado
            if Carné_usuario in plataforma.usuarios:
                print("Ya existe un usuario con ese Carné. Use la opción 2 para acceder.")
                continue

            # Solicita datos personales
            nombre = pedir_nombre()
            email = pedir_email()

            # Crea el objeto correspondiente según el tipo
            if tipo == "E":
                usuario = Estudiante(Carné_usuario, nombre, email)
            elif tipo == "I":
                usuario = Instructor(Carné_usuario, nombre, email)
            else:
                print("Tipo no válido.")
                continue

            # Registra el usuario en la plataforma
            plataforma.registrar_usuario(usuario)
            guardar_usuarios_txt(plataforma)  # Guarda en archivo externo

        elif opcion == "2":
            # Acceso de usuario existente
            Carné_usuario = pedir_Carné()
            usuario = plataforma.usuarios.get(Carné_usuario)

            # Nos manda a los otros menus, dependiendo del tipo de usuario
            if usuario:
                if isinstance(usuario, Estudiante):
                    menu_estudiante(usuario)
                elif isinstance(usuario, Instructor):
                    menu_instructor(usuario, plataforma)
            else:
                print("Usuario no encontrado. Regístrese primero.")

        elif opcion == "3":
            # Cierra el sistema y guarda los cursos
            guardar_cursos_txt(plataforma)
            guardar_notas_txt()
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")

# ============================
# MENÚ ESTUDIANTE
# ============================

def menu_estudiante(estudiante):
    # Ciclo de opciones disponibles para estudiantes
    while True:
        print(f"\n--- MENÚ ESTUDIANTE ({estudiante.nombre}) ---")
        print("1. Ver cursos inscritos")
        print("2. Ver calificaciones")
        print("3. Ver perfil")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Muestra los cursos en los que el estudiante está inscrito
            cursos = estudiante.obtener_cursos_inscritos()
            print("Cursos inscritos:", ", ".join(cursos) if cursos else "Ninguno")

        elif opcion == "2":
            # Muestra las calificaciones registradas
            if estudiante.calificaciones:
                print("Calificaciones:")
                for curso, nota in estudiante.calificaciones.items():
                    print(f" - {curso}: {nota}")
            else:
                print("No hay calificaciones registradas.")

        elif opcion == "3":
            # Muestra el perfil completo del estudiante
            print(estudiante)

        elif opcion == "4":
            # Sale del menú estudiante
            break

        else:
            print("Opción no válida.")        

# ============================
# MENÚ INSTRUCTOR
# ============================

def menu_instructor(instructor, plataforma):
    # Ciclo de opciones disponibles para instructores
    while True:
        print(f"\n--- MENÚ INSTRUCTOR ({instructor.nombre}) ---")
        print("1. Crear curso")
        print("2. Crear evaluación")
        print("3. Asignar calificación a estudiante")
        print("4. Inscribir estudiante en curso")
        print("5. Ver cursos impartidos") 
        print("6. Ver perfil")
        print("7. Ver historial de notas")
        print("8. Generar reporte de promedio bajo")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Crea un nuevo curso y lo asocia al instructor
            codigo = pedir_codigo()
            nombre = pedir_nombre_curso()
            try:
                plataforma.crear_curso(codigo, nombre, instructor.Carné_usuario)
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            # Crea una evaluación para un curso del instructor
            codigo = pedir_codigo()
            curso = plataforma.obtener_info_curso(codigo)
            if curso and curso.instructor == instructor:
                nombre_eval = pedir_nombre_evaluacion()
                tipo_eval = pedir_tipo_evaluacion()

                # Crea el tipo de evaluación correspondiente
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
            # Asigna una nota a un estudiante en una evaluación
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
            # Inscribe un estudiante en un curso del instructor
            Carné_estudiante = pedir_Carné()
            codigo = pedir_codigo()
            estudiante = plataforma.usuarios.get(Carné_estudiante)
            curso = plataforma.cursos.get(codigo)
            if isinstance(estudiante, Estudiante) and curso and curso.instructor == instructor:
                curso.inscribir_estudiante(estudiante)
            else:
                print("Datos inválidos o curso no pertenece al instructor.")

        elif opcion == "5":
            # Muestra los cursos que imparte el instructor
            cursos = instructor.obtener_cursos_impartidos()
            print("Cursos impartidos:", ", ".join(cursos) if cursos else "Ninguno")

        elif opcion == "6":
            # Muestra el perfil completo del instructor
            print(instructor)

        elif opcion == "7":
            # Muestra el historial global de notas registradas
            print("\n--- HISTORIAL DE NOTAS ---")
            for registro in notas:
                print(f"{registro['estudiante']} - {registro['curso']} - {registro['evaluacion']}: {registro['nota']}")

        elif opcion == "8":
            # Genera reporte de estudiantes con promedio bajo en un curso
            codigo = pedir_codigo()
            curso = plataforma.obtener_info_curso(codigo)
            if curso and curso.instructor == instructor:
                reporte_promedio_bajo(curso)
            else:
                print("Curso no encontrado o no pertenece al instructor.")

        elif opcion == "9":
            # Sale del menú instructor
            break

        else:
            print("Opción no válida.")

# ============================
# FUNCIONES PARA GUARDAR INFORMACIÓN EN ARCHIVOS TXT
# ============================

# Funcion para guardar los usuarios
def guardar_usuarios_txt(plataforma, archivo="usuarios.txt"):
    # Guarda todos los usuarios registrados en la plataforma en un archivo de texto
    # Cada línea representa un usuario con sus datos separados por comas
    with open(archivo, "w", encoding="utf-8") as f:
        for usuario in plataforma.usuarios.values():
            # Determina el tipo de usuario (Estudiante o Instructor)
            tipo = "Estudiante" if isinstance(usuario, Estudiante) else "Instructor"

            # Escribe los datos de forma: Carné, nombre, email, tipo
            f.write(f"{usuario.Carné_usuario},{usuario.nombre},{usuario.email},{tipo}\n")

#Funcion para cargar los uusuarios guardados
def cargar_usuarios_txt(plataforma, archivo="usuarios.txt"):
    # Carga los usuarios desde un archivo de texto y los registra en la plataforma
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                # Divide la línea en partes: Carné, nombre, email, tipo
                Carné_usuario, nombre, email, tipo = linea.strip().split(",")

                # Convierte el Carné a entero
                Carné_usuario = int(Carné_usuario)

                # Crea el objeto correspondiente según el tipo
                if tipo == "Estudiante":
                    usuario = Estudiante(Carné_usuario, nombre, email)
                else:
                    usuario = Instructor(Carné_usuario, nombre, email)

                # Registra el usuario en la plataforma
                plataforma.registrar_usuario(usuario)

    except FileNotFoundError:
        # Si el archivo no existe, se informa y se continúa con una plataforma vacía
        print("Archivo de usuarios no encontrado. Se iniciará vacío.")

#Funcion para guardar las notas
def guardar_notas_txt(archivo="notas.txt"):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            f.write("--- HISTORIAL DE NOTAS ---\n")
            for registro in notas:
                f.write(
                    f"Estudiante: {registro['estudiante']} | "
                    f"Curso: {registro['curso']} | "
                    f"Evaluación: {registro['evaluacion']} | "
                    f"Nota: {registro['nota']}\n"
                )
        print(f"Archivo '{archivo}' creado exitosamente con las notas registradas.")
    except Exception as e:
        print(f"Error al guardar las notas: {e}")


#Funcion para guardar los cursos creados
def guardar_cursos_txt(plataforma, archivo="cursos.txt"):
    # Guarda la información completa de todos los cursos en un archivo de texto
    # Incluye código, nombre, instructor, estudiantes inscritos, evaluaciones y extras
    with open(archivo, "w", encoding="utf-8") as f:
        for curso in plataforma.cursos.values():
            f.write(f"--- CURSO ---\n")  
            f.write(f"Código: {curso.codigo}\n")
            f.write(f"Nombre: {curso.nombre}\n")
            f.write(f"Instructor: {curso.instructor.nombre} (Carné: {curso.instructor.Carné_usuario})\n")

            # Lista de estudiantes inscritos
            f.write("Estudiantes inscritos:\n")
            if curso.estudiantes_inscritos:
                for est in curso.estudiantes_inscritos:
                    f.write(f" - {est.nombre} (Carné: {est.Carné_usuario})\n")
            else:
                f.write(" - Ninguno\n")

            # Lista de evaluaciones creadas
            f.write("Evaluaciones:\n")
            if curso.evaluaciones:
                for ev in curso.evaluaciones:
                    f.write(f" - {ev.nombre} ({tipo_de_evaluacion(ev)})\n")
            else:
                f.write(" - Ninguna\n")

            # Información adicional 
            if curso.extra:
                f.write("Información adicional:\n")
                for clave, valor in curso.extra.items():
                    f.write(f" • {clave}: {valor}\n")

            f.write("\n")  # Separador entre cursos

# INICIALIZACIÓN DEL SISTEMA
plataforma = Plataforma()
cargar_usuarios_txt(plataforma)
menu_principal(plataforma)
guardar_notas_txt()  # ← Guarda la nota recién asignada

#COSTO COMENTAR
