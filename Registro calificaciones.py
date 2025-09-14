# REGISTRO DE CALIFICACIONES
def asignar_nota_a_estudiante(curso, evaluacion, estudiante, nota):
    """
    Registra una calificación en una evaluación específica.
    Maneja errores si el estudiante no está inscrito.
    """
    try:
        evaluacion.asignar_nota(estudiante, nota)
        print(f"Nota {nota} asignada a {estudiante.nombre} en {evaluacion.nombre}")
    except ValueError as e:
        print(f"Error al asignar la nota: {e}")