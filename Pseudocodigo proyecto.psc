Proceso PlataformaEducativa
    // Declaración de variables y arreglos principales
    Definir opcion Como Entero
    Dimension usuarios[10000]       // Guarda nombre y correo de cada usuario
    Dimension tipos[10000]          // Guarda el tipo de usuario (E=Estudiante, I=Instructor)
    Dimension cursos[10000]         // Guarda los cursos creados
    Dimension evaluaciones[10000]   // Guarda las evaluaciones creadas
    Dimension notas[10000]          // Guarda notas de los estudiantes
	
    // Bucle principal del sistema
    Repetir
        Escribir "--- MENÚ PRINCIPAL ---"
        Escribir "1. Registrar nuevo usuario"
        Escribir "2. Acceder como usuario existente"
        Escribir "3. Salir"
        Leer opcion
		
        // Menú de opciones principales
        Segun opcion Hacer
            1:
                RegistrarUsuario(usuarios, tipos)  // Registrar estudiante o instructor
            2:
                AccederUsuario(usuarios, tipos, cursos, evaluaciones, notas) // Acceder con ID
            3:
                Escribir "Saliendo del sistema..."
            De Otro Modo:
                Escribir "Opción no válida."
        FinSegun
    Hasta Que opcion = 3
FinProceso


// ==============================
// PROCEDIMIENTOS
// ==============================

SubProceso RegistrarUsuario(usuarios, tipos)
    // Registra un nuevo usuario en el sistema
    Definir id_usuario Como Entero
    Definir nombre, email, tipo Como Cadena
	
    Escribir "Ingrese ID de usuario (1 a 10000): "
    Leer id_usuario
	
    // Validación del rango del ID
    Si id_usuario < 1 O id_usuario > 10000 Entonces
        Escribir "Error: ID fuera de rango."
    FinSi
	
    // Datos del usuario
    Escribir "Ingrese nombre: "
    Leer nombre
    Escribir "Ingrese email: "
    Leer email
    Escribir "¿Tipo de usuario (E=Estudiante, I=Instructor)?"
    Leer tipo
	
    // Guardado en arreglos paralelos
    usuarios[id_usuario] = nombre + " - " + email
    tipos[id_usuario] = tipo
    Escribir "Usuario registrado con éxito."
FinSubProceso


SubProceso AccederUsuario(usuarios, tipos, cursos, evaluaciones, notas)
    // Permite acceder con el ID registrado
    Definir id_usuario Como Entero
    Definir tipo Como Cadena
	
    Escribir "Ingrese el ID de usuario: "
    Leer id_usuario
	
    Si usuarios[id_usuario] <> "" Entonces
        Escribir "Usuario encontrado: ", usuarios[id_usuario], " (", tipos[id_usuario], ")"
		
        tipo = tipos[id_usuario]
		
        // Acceso según el tipo de usuario
        Si tipo = "E" Entonces
            MenuEstudiante(id_usuario, usuarios) // Menú estudiante
        SiNo
            MenuInstructor(id_usuario, usuarios, cursos, evaluaciones, notas) // Menú instructor
        FinSi
    SiNo
        Escribir "Usuario no registrado."
    FinSi
FinSubProceso


// ==============================
// MENÚ ESTUDIANTE
// ==============================
SubProceso MenuEstudiante(id_usuario, usuarios)
    // Opciones disponibles para estudiantes
    Definir opcion Como Entero
    Repetir
        Escribir "--- MENÚ ESTUDIANTE ---"
        Escribir "1. Ver cursos inscritos"
        Escribir "2. Ver calificaciones"
        Escribir "3. Ver perfil"
        Escribir "4. Salir"
        Leer opcion
		
        Segun opcion Hacer
            1:
                Escribir "Cursos inscritos: (simulado)"  // A futuro se pueden guardar
            2:
                Escribir "Calificaciones: (simulado)"    // Igual que arriba
            3:
                Escribir "Perfil: ", usuarios[id_usuario]
            4:
                Escribir "Saliendo del menú estudiante..."
            De Otro Modo:
                Escribir "Opción no válida."
        FinSegun
    Hasta Que opcion = 4
FinSubProceso


// ==============================
// MENÚ INSTRUCTOR
// ==============================
SubProceso MenuInstructor(id_usuario, usuarios, cursos, evaluaciones, notas)
    // Opciones disponibles para instructores
    Definir opcion Como Entero
    Repetir
        Escribir "--- MENÚ INSTRUCTOR ---"
        Escribir "1. Crear curso"
        Escribir "2. Crear evaluación"
        Escribir "3. Asignar calificación a estudiante"
        Escribir "4. Inscribir estudiante en curso"
        Escribir "5. Ver cursos impartidos"
        Escribir "6. Ver perfil"
        Escribir "7. Ver historial de notas"
        Escribir "8. Generar reporte de promedio bajo"
        Escribir "9. Salir"
        Leer opcion
		
        Segun opcion Hacer
            1:
                CrearCurso(cursos, usuarios)  // Crea un curso con código y nombre
            2:
                CrearEvaluacion(evaluaciones, cursos) // Crea examen, tarea o proyecto
            3:
                AsignarNota(usuarios, cursos, evaluaciones, notas) // Registra nota
            4:
                InscribirEstudiante(cursos, usuarios) // Inscribe un estudiante
            5:
                Escribir "Cursos impartidos: (simulado)" 
            6:
                Escribir "Perfil: ", usuarios[id_usuario]
            7:
                Escribir "--- HISTORIAL DE NOTAS ---"
                Para i = 1 Hasta 10000 Con Paso 1 Hacer
                    Si notas[i] <> "" Entonces
                        Escribir notas[i]
                    FinSi
                FinPara
            8:
                Escribir "Reporte de promedio bajo: (simulado)"
            9:
                Escribir "Saliendo del menú instructor..."
            De Otro Modo:
                Escribir "Opción no válida."
        FinSegun
    Hasta Que opcion = 9
FinSubProceso


// ==============================
// FUNCIONES BÁSICAS
// ==============================
SubProceso CrearCurso(cursos, usuarios)
    // Crea un curso asociado a un instructor
    Definir codigo_curso, id_instructor Como Entero
    Definir nombre_curso Como Cadena
	
    Escribir "Ingrese código del curso: "
    Leer codigo_curso
    Escribir "Ingrese nombre del curso: "
    Leer nombre_curso
    Escribir "Ingrese ID del instructor: "
    Leer id_instructor
	
    cursos[codigo_curso] = nombre_curso + " - Instructor: " + usuarios[id_instructor]
    Escribir "Curso creado con éxito."
FinSubProceso


SubProceso CrearEvaluacion(evaluaciones, cursos)
    // Crea una evaluación dentro de un curso
    Definir codigo_curso Como Entero
    Definir nombre_eval, tipo_eval Como Cadena
	
    Escribir "Ingrese código del curso: "
    Leer codigo_curso
    Escribir "Ingrese nombre de la evaluación: "
    Leer nombre_eval
    Escribir "Ingrese tipo de evaluación (Examen/Tarea/Proyecto): "
    Leer tipo_eval
	
    evaluaciones[codigo_curso] = nombre_eval + " - " + tipo_eval
    Escribir "Evaluación creada para curso ", cursos[codigo_curso]
FinSubProceso


SubProceso AsignarNota(usuarios, cursos, evaluaciones, notas)
    // Asigna nota de un estudiante en un curso
    Definir id_estudiante, codigo_curso, nota Como Entero
	
    Escribir "Ingrese ID del estudiante: "
    Leer id_estudiante
    Escribir "Ingrese código del curso: "
    Leer codigo_curso
    Escribir "Ingrese nota (0-100): "
    Leer nota
	
    Si nota >= 0 Y nota <= 100 Entonces
        notas[id_estudiante] = "Nota " + nota + " en " + cursos[codigo_curso]
        Escribir "Nota registrada con éxito."
    SiNo
        Escribir "Error: Nota fuera de rango."
    FinSi
FinSubProceso


SubProceso InscribirEstudiante(cursos, usuarios)
    // Inscribe un estudiante en un curso
    Definir id_estudiante, codigo_curso Como Entero
	
    Escribir "Ingrese ID del estudiante: "
    Leer id_estudiante
    Escribir "Ingrese código del curso: "
    Leer codigo_curso
	
    Escribir "Estudiante ", usuarios[id_estudiante], " inscrito en curso ", cursos[codigo_curso]
FinSubProceso
