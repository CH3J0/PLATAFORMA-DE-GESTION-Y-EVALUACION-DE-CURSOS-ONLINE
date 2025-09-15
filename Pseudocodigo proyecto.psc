Proceso PlataformaEducativa
    Definir opcion Como Entero
    Dimension usuarios[100]
    Dimension cursos[100]
    Dimension evaluaciones[100]
	
    Repetir
        Escribir "--- MENÚ PRINCIPAL ---"
        Escribir "1. Registrar nuevo usuario"
        Escribir "2. Acceder como usuario existente"
        Escribir "3. Crear curso"
        Escribir "4. Inscribir estudiante en curso"
        Escribir "5. Crear evaluación"
        Escribir "6. Asignar nota a estudiante"
        Escribir "7. Mostrar información de curso"
        Escribir "8. Mostrar todos los usuarios"
        Escribir "9. Salir"
        Leer opcion
		
        Segun opcion Hacer
            1:
                RegistrarUsuario(usuarios)
            2:
                AccederUsuario(usuarios)
            3:
                CrearCurso(cursos, usuarios)
            4:
                InscribirEstudiante(cursos, usuarios)
            5:
                CrearEvaluacion(evaluaciones, cursos)
            6:
                AsignarNota(usuarios, cursos, evaluaciones)
            7:
                MostrarCurso(cursos, evaluaciones)
            8:
                MostrarUsuarios(usuarios)
            9:
                Escribir "Saliendo del sistema..."
        FinSegun
    Hasta Que opcion = 9
	
FinProceso


// ==============================
// PROCEDIMIENTOS
// ==============================

SubProceso RegistrarUsuario(usuarios)
    Definir id_usuario Como Entero
    Definir nombre, email, tipo Como Cadena
	
    Escribir "Ingrese ID de usuario: "
    Leer id_usuario
    Escribir "Ingrese nombre: "
    Leer nombre
    Escribir "Ingrese email: "
    Leer email
    Escribir "¿Tipo de usuario (E=Estudiante, I=Instructor)?"
    Leer tipo
	
    usuarios[id_usuario] = nombre + " - " + email + " - " + tipo
    Escribir "Usuario registrado con éxito."
FinSubProceso


SubProceso AccederUsuario(usuarios)
    Definir id_usuario Como Entero
    Escribir "Ingrese el ID de usuario: "
    Leer id_usuario
    Si usuarios[id_usuario] <> "" Entonces
        Escribir "Usuario encontrado: ", usuarios[id_usuario]
    SiNo
        Escribir "Usuario no registrado."
    FinSi
FinSubProceso


SubProceso CrearCurso(cursos, usuarios)
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


SubProceso InscribirEstudiante(cursos, usuarios)
    Definir id_estudiante, codigo_curso Como Entero
	
    Escribir "Ingrese ID del estudiante: "
    Leer id_estudiante
    Escribir "Ingrese código del curso: "
    Leer codigo_curso
	
    Escribir "Estudiante ", usuarios[id_estudiante], " inscrito en curso ", cursos[codigo_curso]
FinSubProceso


SubProceso CrearEvaluacion(evaluaciones, cursos)
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


SubProceso AsignarNota(usuarios, cursos, evaluaciones)
    Definir id_estudiante, codigo_curso, nota Como Entero
	
    Escribir "Ingrese ID del estudiante: "
    Leer id_estudiante
    Escribir "Ingrese código del curso: "
    Leer codigo_curso
    Escribir "Ingrese nota (0-100): "
    Leer nota
	
    Escribir "Nota ", nota, " asignada a ", usuarios[id_estudiante], " en ", cursos[codigo_curso]
FinSubProceso


SubProceso MostrarCurso(cursos, evaluaciones)
    Definir codigo_curso Como Entero
    Escribir "Ingrese código del curso: "
    Leer codigo_curso
	
    Escribir "Información del curso: ", cursos[codigo_curso]
    Escribir "Evaluación: ", evaluaciones[codigo_curso]
FinSubProceso


SubProceso MostrarUsuarios(usuarios)
    Definir i Como Entero
    Escribir "--- LISTA DE USUARIOS REGISTRADOS ---"
    Para i = 1 Hasta 99 Con Paso 1 Hacer
        Si usuarios[i] <> "" Entonces
            Escribir "ID ", i, ": ", usuarios[i]
        FinSi
    FinPara
FinSubProceso
