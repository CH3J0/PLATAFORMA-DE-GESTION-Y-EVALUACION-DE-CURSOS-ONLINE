def tipo_de_evaluacion(evaluacion):
    if isinstance(evaluacion, Examen):
        return "Examen"
    elif isinstance(evaluacion, Tarea):
        return "Tarea"
    elif isinstance(evaluacion, Proyecto):
        return "Proyecto"
    else:
        return "Evaluacion"
    
def reporte_promedio_bajo(curso, umbral=60):
    """
    Genera un reporte de estudiantes con promedio bajo en un curso.
    """
    print(f"\n--- REPORTE: Estudiantes con promedio menor a {umbral} ---")
    for estudiante in curso.estudiantes_inscritos:
        notas = [
            (eval.nombre, tipo_de_evaluacion(eval), eval.notas[estudiante])
            for eval in curso.evaluaciones
            if estudiante in eval.notas
        ]
        if notas:
            promedio = sum(n[2] for n in notas) / len(notas)
            if promedio < umbral:
                print(f"\nEstudiante: {estudiante.nombre} | ID: {estudiante.id_usuario} | Email: {estudiante.email}")
                print(f"Promedio: {promedio:.2f}")
                print("Notas por evaluación:")
                for nombre_eval,tipo, nota in notas:
                    print(f"  - {nombre_eval} ({tipo}): {nota}")