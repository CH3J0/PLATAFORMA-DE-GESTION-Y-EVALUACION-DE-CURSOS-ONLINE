# Historial global de notas asignadas
notas= []

def validar_nota(nota):
    """
    Valida que la nota sea un número entre 0 y 100.
    """
    if not isinstance(nota, (int, float)):
        raise TypeError("La nota debe ser un número")
    if nota < 0 or nota > 100:
        raise ValueError("La nota debe estar entre 0 y 100")

def registrar_historial(estudiante, evaluacion, nota):
    """
    Registra la asignación de nota en el historial.
    """
    notas.append({
        "estudiante": estudiante.nombre,
        "evaluacion": evaluacion.nombre,
        "curso": evaluacion.curso.nombre,
        "nota": nota
    })

def asignar_nota_a_estudiante(evaluacion, estudiante, nota):
    """
    Asigna una nota a un estudiante en cualquier Evaluacion (Examen, Tarea, Proyecto).
    - Valida la nota
    - Llama al método de la evaluación para asignarla
    - Registra la acción en el historial
    """
    try:
        validar_nota(nota)
        evaluacion.asignar_nota(estudiante, nota)
        registrar_historial(estudiante, evaluacion, nota)
        print(f"✅ Nota {nota} asignada a {estudiante.nombre} en {evaluacion.nombre} ({evaluacion.curso.nombre})")
    except (ValueError, TypeError) as e:
        print(f"Error al asignar la nota: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
